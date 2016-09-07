all.ttl:
	riot --out ttl *_dataset.ttl > $@

fetch:
	wget -np -r --accept=dataset.ttl http://data.monarchinitiative.org/ttl/ && mv data.monarchinitiative.org/ttl/*ttl . && rm -rf data.monarchinitiative.org

