monarch.ttl:
	riot --out ttl monarch-datasets/*_dataset.ttl > $@

reports/%.tsv: sparql/%.rq
	arq --query $< --data monarch.ttl --results TSV > $@
