# AV Matrix Message Generator

This tool automates the generation of protocol messages for controlling AV matrix switchers used in professional audio-visual installations.  
I built it to speed up the process of preparing serial/IP control sequences during system commissioning.

### Supported Matrix Brands
- **Kramer** (with optional audio routing)
- **Absolute**

### Why This Tool?
In AV integration workflows, matrix switching commands are often:
- Manufacturer-specific
- Verbose and error-prone to write manually
- Repeated across multiple presets and rooms

This script reduces configuration time and prevents human error during programming and testing.

### Example Usage


Inputs:
1 2 3 4
Outputs:
1 2

In the case of Kramer matrices with audio extraction,
it is necessary to specify which audio outputs are being used.


### Next Planned Features

- Additional AV matrix brands
- GUI frontend for technicians
