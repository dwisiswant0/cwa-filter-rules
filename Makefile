FILTERS_IN := "src/filters.yaml"
FILTERS_OUT := "dist/filters.json"
FILTERS_SCHEMA := "src/filters.schema.json"

lint:
	@yamllint $(FILTERS_IN)

compile: lint
	@yq -o=j $(FILTERS_IN) | jq -c > $(FILTERS_OUT)

test:
	@ajv test -s $(FILTERS_SCHEMA) -d $(FILTERS_OUT) --valid