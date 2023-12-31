import numpy as np
from PIL import Image

def henon_map(x, y, z, a=1.4, b=0.3):
    new_x = 1 - a * x**2 + y
    new_y = b * x
    new_z = 0.5 * z
    return new_x, new_y, new_z

def fractal_function(x, y, z):
    # Any fractal function of our choice can be used
    return np.sin(x) + np.cos(y) + np.sin(z)

def confusion(image):
    flat_pixels = image.flatten()
    indices = np.arange(len(flat_pixels))
    np.random.shuffle(indices)
    shuffled_pixels = flat_pixels[indices].reshape(image.shape)
    return shuffled_pixels

def diffusion(image, x, y, z):
    return np.bitwise_xor(image.astype(np.uint8), np.array([int(x), int(y), int(z)], dtype=np.uint8))

def henon_fractal_encryption(image_path, output_path, a=1.4, b=0.3, iterations=100):
    image = np.array(Image.open(image_path))
    x, y, z = 0.1, 0.2, 0.3
    for i in range(iterations):
        x, y, z = henon_map(x, y, z, a, b)
        fractal_value = fractal_function(x, y, z)
        image = confusion(image)
        image = diffusion(image, x, y, z)
    encrypted_image = Image.fromarray(image.astype(np.uint8))
    encrypted_image.save(output_path)

image_path = '/home/sakresh/Projects/Python/sample_image.png'
output_path = '/home/sakresh/Projects/Python/encrypted_image.png'
henon_fractal_encryption(image_path, output_path)
