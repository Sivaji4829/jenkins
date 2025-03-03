from diffusers import StableDiffusionPipeline
import torch
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


# Load the pre-trained Stable Diffusion model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Define the prompt for image generation
prompt = "a futuristic city and flying car with neon lights"

# Generate the image
image = pipe(prompt).images[0]

# Save the generated image
image.save("generated_image.png")

# Display the image if desired (optional)
image.show()