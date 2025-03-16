import kagglehub

# Downloading the dataset
path = kagglehub.dataset_download(handle="osmi/mental-health-in-tech-2016")

print("Path to dataset files:", path)