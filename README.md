# QwenAgent-Interface
Project Status: Alpha; under development. It does not work yet....

### Current Work
1. Completing the scripts...
- if we only monitor system memory usage, then by using only vulkan, would mean the program is compatible with any vulkan card, though it will be up to the user to ensure the graphics card is able to take the load of each model individually (ie, ensure to use solid color on desktop, and dont load any games, if its a card you are using). Maybe there is a library for monitoring the GPU though vulkan?
- Streamline the installer to only install, requirements and the vulkan llama.cpp library. 
- Determine if all the code is implemented correctly, by going over qwen-agent tutorials/examples.
- pretty sure the llama.cpp code is mostly there, however we do want to examine the syntax, and ensure we utilize arguments in the command lines optimally and correctly.
- We do want to take advantage of the features in the framework, ensure to investigate framework examples further, and at the same correct any errors.
2. Bugfix scripts to a bug free version that can startup and shutdown.
3. Complete Gradio Interface, does it work with win 10 python 3.12, what can we expect, what are possibilities.
4. investigave correct operation through gradio interface, ensuare all features working correctly.
5. Improve and Expand...

- agents able to work in parrellel, each having, a copy of the same model.
- Further updates to UI, to integrate all improvements somehow.
- After code context begins to become an issue, then optimize and make more dynamic and compacted, the functions. 
- Other Llama.cpp binaries available need researching again, and integrating into the configurator.
- a youtube demonstration video, to gain interest and guide people.
- New name Possibly, QAgent-CppAgi, QwenAgent-CppCore, ??

## Description:
- Currently a project to produce, a, Gradio and QwenAgent and LlamaCpp, based Agent Manager, capable of managing text or code based projects, to completion, for all that would be useful or interesting. Utilizing the best solutions I can find from research etc. Unfortunately it turns out the AMD on windows is still limited even with DirectML, because that only works on certain AMD hardware with windows. So we are reverting to llama.cpp, and inadvertantly finding llama.cpp does now infact feature vulkan, and has been for a while, this saves the project for me, but also makes me wonder why ollama is not using this, as it uses llamacpp binaries too doesnt it?

### Features:
- Gpu-Compatibility :- Runs on, nVidia and Amd (inc non-ROCm), through new Vulkan Llama.cpp Binaries.
- Multi-Model :- using 3 gguf models, chat, instruct, code, loaded to Ram at start, then GPU on demand.
- Simple Operation :- No requirement of, Ollama or LMStudio, as using Llama.cpp pre-compiled binaries.
- Standalone Installer Tool, for pre-launch installation, for pip requirements and github libraries.
- Monitoring of system memory usage with auto-unload, to ensure system is not over-loaded by data.
 
### Preview:
- Dunno how I am going to show the main program, possibly get a image to text converter or resurrect my webspace, here is improvised content to demonstrate the concept...
```
===== Some Impressive Bot Management Program =======

HUMAN:
I neez some fags, make a plan, and get me some, so I can
sit in my chair, and finish my project without thinking
about how life is passing by.
--------------------------------------------
ROBOT1:
My prime directive is to go to the shops,
and buy 10 fags, do you compute.
-----------------------------------------
ROBOT2:
Designing fake hair and beard for ROBOT1, so it can blend-in
with the other humans, during travel to the shop.
----------------------------------------
ROBOT3:
By growing tobacco, we will have our own source of
tobacco in a few months, and no-longer be exploited.

```
- Standalone Configurator, for pre-launch setup...
```

========================( Setup-Installer )=======================







                     1. Install Requirements
                (pip install -r requirements.txt)

                   2. Install GitHub Libraries
                        (Llama.Cpp: b3206)






-----------------------------------------------------------------
Selection; Choose Options = 1-2, Exit Config = X:

```

## Requirements:
- Vulkan compatible Graphics Card with 8GB+, a graphics card with enough vram to individually load the models you choose (including any display usage, in which case I advise, solid color desktop and shut down media intensive apps).
- System Memory 32GB+, enough system memory to load all 3 of the models you choose AT THE SAME TIME.
- Python, Developed on [Python 3.12.x](https://www.python.org/downloads/release/python-3120/?ref=upstract.com) Non-WSL, untested on others.
- [Windows](https://www.ebay.co.uk/b/bn_2683753), most will work, but its developed on Windows 10.
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with "Desktop development with C++" installed, so pip can install things like `pyamdgpuinfo`.
- [Qwen-Agent Framework](https://github.com/QwenLM/Qwen-Agent), without dropping my files into that, they wont work.
- [Requirements.txt](https://github.com/wiseman-timelord/QwenAgent-Interface/blob/main/requirements.txt), mostly from the framework, are installed by the configurator.
- Other libraries, such as [llama.cpp pre-compiled binaries](https://github.com/ggerganov/llama.cpp/releases), are installed by the configurator.


### Instructions:
- Releases are considered non-working, but here are the early instructions...
1. Ensure you are on Windows, and are not using Wsl to run python, unless you know some other method of emulating windows python.
2. Ensure you have Installed the requirements detailed above, for, C++ Build Tools and Python.
3. Download [Qwen-Agent Framework](https://github.com/QwenLM/Qwen-Agent) into a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files directly to that folder.
4. Drop in my scripts for QwenAgent-Interface directly into "Qwen-Agent-0.0.5+" preserving file structure, and relevantly over-writing the "requirements.txt".
5. Install remaining, requirements and libraries, through "QwenAgent-Configure.Bat", and setup the model used and tweak max memory if you feel the need.
6. Run "QwenAgent-Launcher.Bat" to start the session. 

### Notes:
- Developed for and testing on, Matisse CPU with 64GB for 57B models and 8GB Artic Islands GPU for 7b models .

## Credits:
- The producers of...Llama.cpp, Vulkan, Qwen-Agent Framework, Qwen2 series language models...make my project possible.


