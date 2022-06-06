folder_output="brand-colors"

generate_palete:
	@echo "Generating palette..."
	python main.py
	@echo "Palette generated"

compress_paletes:
	@echo "Compressing palette..."
	zip -r $(folder_output).zip $(folder_output)
	rm -rf $(folder_output)
	@echo "Brand colors compressed"