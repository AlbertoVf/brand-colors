folder_output="brand-colors"

generate_palete:
	@echo "Generating palete..."
	wget --output-document $(folder_output)/brandcolors.scss 'http://brandcolors.net/download/?f=scss'
	python src/main.py
	@echo "Palete generated"

compress_paletes:
	@echo "Compressing palete..."
	zip -r $(folder_output).zip $(folder_output)
	@echo "Brand colors compressed"

clean_output:
	@echo "Cleaning output..."
	rm -rf $(folder_output)
	@echo "Output cleaned"