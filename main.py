from ascii_art.converter import ImageToAscii
from ascii_art.utils import validate_file_path, create_output_directory

def main():
    image_path = input("File path: ")
    output_dir = "output"
    output_width = int(input("Width: "))
    

    try:
        validate_file_path(image_path)
    except FileNotFoundError as e:
        print(e)
        return
    
    create_output_directory(output_dir)
    
    # ASCII conversion
    converter = ImageToAscii()
    ascii_art = converter.convert_image_to_ascii(image_path, output_width=output_width)
    
    # Save the ASCII art to a file
    output_file = f"{output_dir}/ascii_art.txt"
    with open(output_file, "w") as f:
        f.write(ascii_art)
    print("\nASCII art succesfully produced:")
    print(output_file)

if __name__ == "__main__":
    main()