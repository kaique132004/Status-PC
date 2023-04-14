import psutil

def display_memory_info():
    mem = psutil.virtual_memory()
    mem_total = mem.total / 1024 / 1024
    mem_avail = mem.available / 1024 / 1024
    print(f"Memory usage:\n  Total physical memory: {mem_total:.2f} MB\n  Free physical memory: {mem_avail:.2f} MB")

def display_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage:\n  {cpu_percent:.2f} %")

def display_disk_info():
    disk_usage = psutil.disk_usage('/')
    disk_total = disk_usage.total / 1024 / 1024 / 1024
    disk_used = disk_usage.used / 1024 / 1024 / 1024
    print(f"Disk usage:\n  Total disk space: {disk_total:.2f} GB\n  Used disk space: {disk_used:.2f} GB")

def display_network_info():
    net_io_counters = psutil.net_io_counters()
    bytes_sent = net_io_counters.bytes_sent / 1024
    bytes_recv = net_io_counters.bytes_recv / 1024
    print(f"Network usage:\n  Bytes sent: {bytes_sent:.2f} KB\n  Bytes received: {bytes_recv:.2f} KB")

if __name__ == '__main__':
    display_memory_info()
    display_cpu_info()
    display_disk_info()
    display_network_info()