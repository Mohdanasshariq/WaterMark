from PIL import Image

def add_watermark(original_image_path, watermark_image_path, output_image_path):
    # Load the original image and watermark image
    original_image = Image.open(original_image_path).convert('RGBA')
    watermark_image = Image.open(watermark_image_path).convert('RGBA')

    # Get the dimensions of the original image
    mediabox_width, mediabox_height = original_image.size

    # Get the dimensions of the watermark image
    watermark_width, watermark_height = watermark_image.size

    # Calculate the desired size for the watermark
    max_width = mediabox_width // 4  # Adjust as desired
    max_height = mediabox_height // 4  # Adjust as desired

    # Scale the watermark image to fit within the desired dimensions
    watermark_ratio = min(max_width / watermark_width, max_height / watermark_height)
    new_watermark_width = int(watermark_width * watermark_ratio)
    new_watermark_height = int(watermark_height * watermark_ratio)
    watermark_image = watermark_image.resize((new_watermark_width, new_watermark_height))

    # Calculate the shift values
    shift_x = mediabox_width - new_watermark_width
    shift_y = mediabox_height - new_watermark_height

    # Create a new image with the watermark in the bottom right corner
    new_image = original_image.copy()
    new_image.paste(watermark_image, (shift_x, shift_y), watermark_image)

    # Save the output image
    new_image.save(output_image_path)

# Usage example:
original_image_path = 'input-onlinejpgtools.jpg'
watermark_image_path = 'index.png'
output_image_path = 'output_image.png'

add_watermark(original_image_path, watermark_image_path, output_image_path)
