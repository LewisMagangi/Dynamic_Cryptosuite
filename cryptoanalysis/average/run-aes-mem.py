import subprocess

data_sizes = [1, 2, 5, 10, 20, 50]
sample_text_folder = './sample-text/'

for data_size in data_sizes:
    file_name = f'{data_size}_mb_text_data_faker.txt'
    command = f'python -m memory_profiler average-aes-time-mem.py {sample_text_folder}{file_name}'
    subprocess.run(command, shell=True)