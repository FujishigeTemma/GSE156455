import ipywidgets as widget
from IPython.display import display


def multi_checkbox_widget(options_dict):
    """Widget with a search field and lots of checkboxes"""
    search_widget = widget.Text()
    output_widget = widget.Output()
    options = [x for x in options_dict.values()]
    options_layout = widget.Layout(overflow="auto", border="1px solid black", width="300px", height="300px", flex_flow="column", display="flex")

    options_widget = widget.VBox(options, layout=options_layout)
    multi_select = widget.VBox([search_widget, options_widget])

    @output_widget.capture()
    def on_checkbox_change():
        options_widget.children = sorted([x for x in options_widget.children], key=lambda x: x.value, reverse=True)

    for checkbox in options:
        checkbox.observe(on_checkbox_change, names="value")

    # Wire the search field to the checkboxes
    @output_widget.capture()
    def on_text_change(change):
        search_input = change["new"]
        if search_input == "":
            # Reset search field
            new_options = sorted(options, key=lambda x: x.value, reverse=True)
        else:
            # Filter by search field using difflib.
            # close_matches = difflib.get_close_matches(search_input, list(options_dict.keys()), cutoff=0.0)
            close_matches = [x for x in list(options_dict.keys()) if str.lower(search_input.strip("")) in str.lower(x)]
            new_options = sorted([x for x in options if x.description in close_matches], key=lambda x: x.value, reverse=True)  # [options_dict[x] for x in close_matches]
        options_widget.children = new_options

    search_widget.observe(on_text_change, names="value")
    display(output_widget)
    return multi_select


def f(**args):
    results = [key for key, value in args.items() if value]
    display(results)


def create_multiple_checkbox_widget(options):
    options_dict = {x: widget.Checkbox(description=x, value=False, style={"description_width": "0px"}) for x in options if x}
    ui = multi_checkbox_widget(options_dict)
    out = widget.interactive_output(f, options_dict)
    display(widget.HBox([ui, out]))

    return ui
