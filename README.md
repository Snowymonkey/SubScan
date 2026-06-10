# SubScan

`SubScan` is a high-speed, multi-threaded command-line subdomain enumeration tool written in Python. It allows users to quickly perform small, medium, or large subdomain scans using configurable threading for efficient discovery.

## Features

* **Multi-Threaded Performance:** Uses configurable thread pools to speed up subdomain enumeration.
* **Tiered Scanning Modes:** Supports small, medium, and large scans for different wordlist sizes.
* **Configurable Thread Count:** The number of worker threads is controlled through `config.json`.

---

## Installation

Clone or download this repository to your local machine:

   ```bash
   git clone https://github.com/Snowymonkey/SubScan
   cd SubScan
   ```
## Usage

| Argument | Description |
|-----------|------------|
| `-s`, `--small_scan` | Small top 5000 subdomain scan |
| `-m`, `--medium_scan` | Medium top 20000 subdomain scan |
| `-l`, `--large_scan` | Large top 110000 subdomain scan |
| `--help` | Help information of all arguments |

### Small subdomain scan
```bash
python subscan.py --small_scan example.com
python subscan.py -s example.com
```
### Medium subdomain scan
```bash
python subscan.py --medium_scan example.com
python subscan.py -m example.com
```
## Large subdomain scan
```bash
python subscan.py --large_scan example.com
python subscan.py -l example.com
```
After the scan the program will create a report file showing all valid subdomains for the website.

calendar.google.com : 142.250.189.110
survey.google.com : 142.251.210.238
jobs.google.com : 2607:f8b0:4009:80d::200e
ipv6.google.com : 2607:f8b0:4009:80d::200e
registry.google.com : 142.250.217.110
edu.google.com : 142.251.41.78
uploads.google.com : 108.170.217.160
station.google.com : 2607:f8b0:4009:80d::200e
activity.google.com : 2607:f8b0:4001:c6c::71

## Notes

If you suspect that your network is dropping your packets, it may be due to the high thread count. You can easily change this in the config.json file, set with the `max_threads` parameter.
