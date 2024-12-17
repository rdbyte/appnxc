import os
import shiv

output_file = "bin/nxc"
source_dir = "src"  

if not os.path.exists("bin"):
    os.makedirs("bin")

print("Building ZipApp...")
shiv.create_archive(
    site_packages=source_dir,
    entry_point="__main__:main",
    target=output_file,
    compressed=True
)
print(f"ZipApp generated: {output_file}")
