# import conda_build.source
from conda.gateways.disk.read import compute_sum

print(compute_sum("/Users/kimshan/Public/library/plotnn/src/dist/plotnn-0.1.0.tar.gz", "sha256"))