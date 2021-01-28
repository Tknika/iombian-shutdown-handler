# IoMBian Shutdown Handler

This service listens to a "long_click" event from a ZeroMQ publisher and shuts down the device.

## Installation

- Clone the repo into a temp folder:

> ```git clone https://github.com/Tknika/iombian-shutdown-handler.git /tmp/iombian-shutdown-handler && cd /tmp/iombian-shutdown-handler```

- Create the installation folder and move the appropiate files (edit the user):

> ```sudo mkdir /opt/iombian-shutdown-handler```

> ```sudo cp requirements.txt /opt/iombian-shutdown-handler```

> ```sudo cp -r src/* /opt/iombian-shutdown-handler```

> ```sudo cp systemd/iombian-shutdown-handler.service /etc/systemd/system/```

> ```sudo chown -R iompi:iompi /opt/iombian-shutdown-handler```

- Create the virtual environment and install the dependencies:

> ```cd /opt/iombian-shutdown-handler```

> ```python3 -m venv venv```

> ```source venv/bin/activate```

> ```pip install --upgrade pip```

> ```pip install -r requirements.txt```

- Start the script

> ```sudo systemctl enable iombian-shutdown-handler.service && sudo systemctl start iombian-shutdown-handler.service```

## Author

(c) 2021 [Aitor Iturrioz Rodríguez](https://github.com/bodiroga)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.