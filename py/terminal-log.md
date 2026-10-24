PowerShell 7.6.8
PS C:\Windows\System32> pip install --no-cache-dir `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz
Defaulting to user installation because normal site-packages is not writeable
Collecting rocm-sdk-core==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl (644.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 644.8/644.8 MB 45.0 MB/s eta 0:00:00
Collecting rocm-sdk-devel==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl (232.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.8/232.8 MB 33.6 MB/s eta 0:00:00
Collecting rocm-sdk-libraries-custom==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl (490.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 490.0/490.0 MB 44.2 MB/s eta 0:00:00
Collecting https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz (15 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: rocm
  Building wheel for rocm (pyproject.toml) ... done
  Created wheel for rocm: filename=rocm-7.2.1-py3-none-any.whl size=20088 sha256=6505fc7d6b031113f43118c0ae57ac82f56326bc7bec1308eb6ddc1372a4b499
  Stored in directory: C:\Users\geonwoo\AppData\Local\Temp\pip-ephem-wheel-cache-i96d3m92\wheels\5f\25\fa\64c630e6b07d94199c5751c182617b4309379b85c58146d540
Successfully built rocm
Installing collected packages: rocm-sdk-libraries-custom, rocm-sdk-devel, rocm-sdk-core, rocm
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\geonwoo\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python312\\site-packages\\_rocm_sdk_libraries_custom\\bin\\hipblaslt\\library\\TensileLibrary_B8B8_B8B8_HA_Bias_SAB_SCD_SAV_UA_Type_B8B8_HPA_Contraction_l_Ailk_Bjlk_Cijk_Dijk_gfx1200.co'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths


[notice] A new release of pip is available: 25.0.1 -> 26.2.2
[notice] To update, run: C:\Users\geonwoo\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Windows\System32> New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" `
>> -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
New-ItemProperty: Requested registry access is not allowed.
PS C:\Windows\System32> pip install --no-cache-dir `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz
Defaulting to user installation because normal site-packages is not writeable
Collecting rocm-sdk-core==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_core-7.2.1-py3-none-win_amd64.whl (644.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 644.8/644.8 MB 35.7 MB/s eta 0:00:00
Collecting rocm-sdk-devel==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_devel-7.2.1-py3-none-win_amd64.whl (232.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 232.8/232.8 MB 41.2 MB/s eta 0:00:00
Collecting rocm-sdk-libraries-custom==7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm_sdk_libraries_custom-7.2.1-py3-none-win_amd64.whl (490.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 490.0/490.0 MB 44.1 MB/s eta 0:00:00
Collecting https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/rocm-7.2.1.tar.gz (15 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: rocm
  Building wheel for rocm (pyproject.toml) ... done
  Created wheel for rocm: filename=rocm-7.2.1-py3-none-any.whl size=20088 sha256=92f1ad3bac02574f694cda23e5ec3de4189d2ffa0632502a20ffe00b23624d0b
  Stored in directory: C:\Users\geonwoo\AppData\Local\Temp\pip-ephem-wheel-cache-beq1uc37\wheels\5f\25\fa\64c630e6b07d94199c5751c182617b4309379b85c58146d540
Successfully built rocm
Installing collected packages: rocm-sdk-libraries-custom, rocm-sdk-devel, rocm-sdk-core, rocm
  WARNING: The scripts amdclang++.exe, amdclang-cl.exe, amdclang-cpp.exe, amdclang.exe, amdflang.exe, amdlld.exe, hipInfo.exe, hipcc.exe, hipconfig.exe, hipify-clang.exe, offload-arch.exe, roc-obj-extract.exe, roc-obj-ls.exe and roc-obj.exe are installed in 'C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script rocm-sdk.exe is installed in 'C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed rocm-7.2.1 rocm-sdk-core-7.2.1 rocm-sdk-devel-7.2.1 rocm-sdk-libraries-custom-7.2.1

[notice] A new release of pip is available: 25.0.1 -> 26.2.2
[notice] To update, run: C:\Users\geonwoo\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Windows\System32> pip install --no-cache-dir `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torch-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchaudio-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl `
>>     https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchvision-0.24.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl
Defaulting to user installation because normal site-packages is not writeable
Collecting torch==2.9.1+rocm7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torch-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl (821.1 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 821.1/821.1 MB 41.8 MB/s eta 0:00:00
Collecting torchaudio==2.9.1+rocm7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchaudio-2.9.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl (514 kB)
Collecting torchvision==0.24.1+rocm7.2.1
  Downloading https://repo.radeon.com/rocm/windows/rocm-rel-7.2.1/torchvision-0.24.1%2Brocm7.2.1-cp312-cp312-win_amd64.whl (1.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.9/1.9 MB 106.7 MB/s eta 0:00:00
Collecting filelock (from torch==2.9.1+rocm7.2.1)
  Downloading filelock-4.2.4-py3-none-any.whl.metadata (2.0 kB)
Collecting typing-extensions>=4.10.0 (from torch==2.9.1+rocm7.2.1)
  Downloading typing_extensions-4.16.0-py3-none-any.whl.metadata (3.3 kB)
Collecting setuptools (from torch==2.9.1+rocm7.2.1)
  Downloading setuptools-84.2.1-py3-none-any.whl.metadata (6.6 kB)
Collecting sympy>=1.13.3 (from torch==2.9.1+rocm7.2.1)
  Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting networkx>=2.5.1 (from torch==2.9.1+rocm7.2.1)
  Downloading networkx-3.7-py3-none-any.whl.metadata (6.7 kB)
Collecting jinja2 (from torch==2.9.1+rocm7.2.1)
  Downloading jinja2-3.1.6-py3-none-any.whl.metadata (2.9 kB)
Collecting fsspec>=0.8.5 (from torch==2.9.1+rocm7.2.1)
  Downloading fsspec-2026.9.0-py3-none-any.whl.metadata (10 kB)
Requirement already satisfied: rocm==7.2.1 in c:\users\geonwoo\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from rocm[libraries]==7.2.1->torch==2.9.1+rocm7.2.1) (7.2.1)
Requirement already satisfied: rocm-sdk-core==7.2.1 in c:\users\geonwoo\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from rocm==7.2.1->rocm[libraries]==7.2.1->torch==2.9.1+rocm7.2.1) (7.2.1)
Requirement already satisfied: rocm-sdk-libraries-custom==7.2.1 in c:\users\geonwoo\appdata\local\packages\pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0\localcache\local-packages\python312\site-packages (from rocm[libraries]==7.2.1->torch==2.9.1+rocm7.2.1) (7.2.1)
Collecting numpy (from torchvision==0.24.1+rocm7.2.1)
  Downloading numpy-2.5.4-cp312-cp312-win_amd64.whl.metadata (6.6 kB)
Collecting pillow!=8.3.*,>=5.3.0 (from torchvision==0.24.1+rocm7.2.1)
  Downloading pillow-13.0.0-cp312-cp312-win_amd64.whl.metadata (9.3 kB)
Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch==2.9.1+rocm7.2.1)
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch==2.9.1+rocm7.2.1)
  Downloading markupsafe-3.0.4-cp312-cp312-win_amd64.whl.metadata (2.8 kB)
Downloading fsspec-2026.9.0-py3-none-any.whl (221 kB)
Downloading networkx-3.7-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 60.6 MB/s eta 0:00:00
Downloading pillow-13.0.0-cp312-cp312-win_amd64.whl (7.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.3/7.3 MB 56.1 MB/s eta 0:00:00
Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 64.2 MB/s eta 0:00:00
Downloading typing_extensions-4.16.0-py3-none-any.whl (45 kB)
Downloading filelock-4.2.4-py3-none-any.whl (162 kB)
Downloading jinja2-3.1.6-py3-none-any.whl (134 kB)
Downloading numpy-2.5.4-cp312-cp312-win_amd64.whl (12.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 12.6/12.6 MB 65.5 MB/s eta 0:00:00
Downloading setuptools-84.2.1-py3-none-any.whl (876 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 876.3/876.3 kB ? eta 0:00:00
Downloading markupsafe-3.0.4-cp312-cp312-win_amd64.whl (14 kB)
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB ? eta 0:00:00
Installing collected packages: mpmath, typing-extensions, sympy, setuptools, pillow, numpy, networkx, MarkupSafe, fsspec, filelock, jinja2, torch, torchvision, torchaudio
  WARNING: The script isympy.exe is installed in 'C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts f2py.exe and numpy-config.exe are installed in 'C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The scripts torchfrtrace.exe and torchrun.exe are installed in 'C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed MarkupSafe-3.0.4 filelock-4.2.4 fsspec-2026.9.0 jinja2-3.1.6 mpmath-1.3.0 networkx-3.7 numpy-2.5.4 pillow-13.0.0 setuptools-84.2.1 sympy-1.14.0 torch-2.9.1+rocm7.2.1 torchaudio-2.9.1+rocm7.2.1 torchvision-0.24.1+rocm7.2.1 typing-extensions-4.16.0

[notice] A new release of pip is available: 25.0.1 -> 26.2.2
[notice] To update, run: C:\Users\geonwoo\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip
PS C:\Windows\System32>
PS C:\Windows\System32> python -c "import torch" 2>nul && echo Success || echo Failure
[WARNING] failed to run offload-arch: binary not found.
PS C:\Windows\System32> python -c "import torch; print('IMPORT_OK'); print('torch:', torch.__version__); print('HIP:', torch.version.hip); print('CUDA:', torch.version.cuda)"
[WARNING] failed to run offload-arch: binary not found.
IMPORT_OK
torch: 2.9.1+rocm7.2.1
HIP: 7.2.53211-158bd99533
CUDA: None
PS C:\Windows\System32> Write-Output "ExitCode=$LASTEXITCODE"where offload-arch
ExitCode=0
where
offload-arch
PS C:\Windows\System32> python -c "import torch; print('IMPORT_OK')"
[WARNING] failed to run offload-arch: binary not found.
IMPORT_OK
PS C:\Windows\System32> python -c "import torch" 2>nul && echo Success || echo Failure
[WARNING] failed to run offload-arch: binary not found.
Success
PS C:\Windows\System32> where.exe offload-arch
INFO: Could not find files for the given pattern(s).
PS C:\Windows\System32> Get-Command offload-arch -ErrorAction SilentlyContinue
PS C:\Windows\System32> $base = "$env:LOCALAPPDATA\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312"
PS C:\Windows\System32> Get-ChildItem -Path $base -Recurse -Filter offload-arch.exe -ErrorAction SilentlyContinue | Select-Object -ExpandProperty FullName
C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\offload-arch.exe
C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\site-packages\_rocm_sdk_core\lib\llvm\bin\offload-arch.exe
PS C:\Windows\System32> where.exe offload-arch
INFO: Could not find files for the given pattern(s).
PS C:\Windows\System32> python -c "import torch; print('IMPORT_OK')"
[WARNING] failed to run offload-arch: binary not found.
IMPORT_OK
PS C:\Windows\System32> $scripts = "$base\Scripts"
PS C:\Windows\System32> $env:Path = "$env:Path;$scripts"
PS C:\Windows\System32> where.exe offload-arch
C:\Users\geonwoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts\offload-arch.exe
PS C:\Windows\System32> python -c "import torch; print('IMPORT_OK')"
IMPORT_OK
PS C:\Windows\System32> $scripts = "$env:LOCALAPPDATA\Packages\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\LocalCache\local-packages\Python312\Scripts"
PS C:\Windows\System32> $userPath = [Environment]::GetEnvironmentVariable("Path","User")
PS C:\Windows\System32> if ($userPath -notlike "*$scripts*") {
>>   [Environment]::SetEnvironmentVariable("Path", "$userPath;$scripts", "User")
>> }
PS C:\Windows\System32> python -c "import torch; print(torch.cuda.is_available())"
True
PS C:\Windows\System32> python -c "import torch; print(f'device name [0]:', torch.cuda.get_device_name(0))"
device name [0]: AMD Radeon RX 9070 XT
PS C:\Windows\System32> python -m torch.utils.collect_env
<frozen runpy>:128: RuntimeWarning: 'torch.utils.collect_env' found in sys.modules after import of package 'torch.utils', but prior to execution of 'torch.utils.collect_env'; this may result in unpredictable behaviour
Collecting environment information...
PyTorch version: 2.9.1+rocm7.2.1
Is debug build: False
CUDA used to build PyTorch: N/A
ROCM used to build PyTorch: 7.2.53211-158bd99533

OS: Microsoft Windows 11 Pro (10.0.26300 64-bit)
GCC version: Could not collect
Clang version: Could not collect
CMake version: Could not collect
Libc version: N/A

Python version: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] (64-bit runtime)
Python platform: Windows-11-10.0.26300-SP0
Is CUDA available: True
CUDA runtime version: Could not collect
CUDA_MODULE_LOADING set to:
GPU models and configuration: AMD Radeon RX 9070 XT (gfx1201)
Nvidia driver version: Could not collect
cuDNN version: Could not collect
Is XPU available: False
HIP runtime version: 7.2.53211
MIOpen runtime version: 3.5.1
Is XNNPACK available: True

CPU:
Name: AMD Ryzen 7 9700X 8-Core Processor
Manufacturer: AuthenticAMD
Family: 107
Architecture: 9
ProcessorType: 3
DeviceID: CPU0
CurrentClockSpeed: 3800
MaxClockSpeed: 3800
L2CacheSize: 8192
L2CacheSpeed: None
Revision: 17408

Versions of relevant libraries:
[pip3] numpy==2.5.4
[pip3] torch==2.9.1+rocm7.2.1
[pip3] torchaudio==2.9.1+rocm7.2.1
[pip3] torchvision==0.24.1+rocm7.2.1
[conda] Could not collect