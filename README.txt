The final dataset is provided in following format:
- data is provided separately for the main (24-96h APF) and the early datasets (0-24h APF)
- filenames include corresponding suffix: _main or _early
- cells from 24h APF are present in both datasets

1) Raw gene counts in 10X genomics format (note that filenames include _main/_early suffixes):
- matrix_main.mtx.gz: sparse matrix in MEX format
- barcodes_main.tsv: modified cell barcodes (see cellID format below)
- features_early.tsv.gz: gene names

2) Metadata for single-cell transcriptomes:
- metadata_main.tsv.gz:
	barcode: cellID
	set: W1118 or DGRP datasets
	rep: biological replicate (A/B)
	trep: technical replicate (i.e. a single 10X library, see sampleID format below)
	genotype: W1118 or DGRP strain (based on demultiplexing)
	time: timepoint
	class: cell class
	type: cell type or cluster identity
	subtype: cell subtype (if not applicable, same as type)

3) tSNE embeddings:
- tsne_main.tsv.gz:
	barcode: cellID
	tSNE_1: cell projection on tSNE 1
	tSNE_2: cell projection on tSNE 2

sampleID:
- sampleID format: set_timepoint_biorep_techrep (e.g. W1118_24h_A_1)
- technical replicates corresponds to a single 10X library and separate raw data files
- DGRP samples includes all timepoints, thus timepoint is indicated as All (e.g. DGRP_All_A_1)
- cellID format: sampleID_barcode (e.g. DGRP_All_A_3_GCGGAAAGTGGTCTCG)

UPDATES:

11/02/20
- Correction of cluster labels for T4/T5 subtypes:
  Labels for T4c and T4d subtype clusters were swapped (T4c <-> T4d).
  Files affected: metadata_main.tsv.gz
