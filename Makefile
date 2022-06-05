folder_output="brand-colors"

generate_palete:
	@echo "Generating palete..."
	python src/main.py
	@echo "Palete generated"

download_palete:
	@echo "Downloading palete..."
	wget --output-document $(folder_output)/brandcolors.scss 'http://brandcolors.net/download/?f=scss'
	@echo "Palete downloaded"

compress_paletes:
	@echo "Compressing palete..."
	zip -r $(folder_output).zip $(folder_output)
	@echo "Brand colors compressed"