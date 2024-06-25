# QAgent-CppAgi
Project Status: Alpha; under development. It does not work yet....

### Current Work
1. Completing the scripts...
- next version of utility_general.py will be big, ensure to refractor code for loading/unloading models to a new script ".\scripts\model_manager.py", specifically for loading/saving models to gpu/system ram.
- rename "menu_display" to "display_gradio", in find in files replacement.
- need to find how many layers a model has, then devide the number of layers by the size of the model, then use this as a guage as to how many complete layers it is safe to offload to the GPU, given the current load on the GPU, and then load only that number of layers, and the rest to system ram. also subtract something for the "maximum_memory_usage".
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
- Currently a project to produce, a, Gradio and QwenAgent and LlamaCpp, based Agent Manager, capable of managing text or code based projects, to completion, for all that would be useful or interesting. Utilizing the best solutions I can find from research etc. Unfortunately it turned out the AMD on windows is still limited even with DirectML because it requires ROCm. However, as it turns out, there are Vulkan versions of llama.cpp, I have done stuff with llama.cpp before.

### Features:
- Gpu-Compatibility :- Runs on Amd (inc non-ROCm) through new Vulkan Llama.cpp Binaries.
- Multi-Model :- using 3 gguf models, chat, instruct, code, loaded to Ram at start, then GPU on demand.
- Simple Operation :- No requirement of, Ollama or LMStudio, as using Llama.cpp pre-compiled binaries.
- Standalone Installer Tool, for pre-launch installation, for pip requirements and github libraries.
- Monitoring of, VRam and Ram, usage with auto-unload, to prevent overload, offloading layers is being worked on.
 
### Preview:
- This is a purely conceptual blueprint, at this stage.
```
=============== QAgent-CppAgi ================
----------------------------------------------------
HUMANOID:
---------------------------------------------------
I want you to update the files for the interface we are using, please do X to the Y script, then produce relating required updates for the other relevant code, then save the file, and restart the interface.
----------------------------------------------------
--------------------------------------------
AI-CHAT:
-------------------------------------------
Research: Found relevant training data, it says A. 
Produced relevant web-research for doing X to the Y script.
Ordering AI-INST to assemble the data from C. 
Assessing Data, the research stated B.
Ordering AI-CODE to produce the relevant updates using information D.
Operation has been completed, file is saved.
Unloading all loaded models.
Shutting down interface in 10 seconds.
--------------------------------------------
-----------------------------------------
AI-INST:
--------------------------------------------
New order from AI-CHAT, getting on with order.
Data Assembled, as instructed.
Data Passed on to AI-CHAT.
Functions replaced in script and file saved.
Passing complete script to AI-CODE.
----------------------------------------
--------------------------------------------
AI-CODE:
----------------------------------------------------
Analyzing Current Code and relevant information.
Analyzing current code and producing updates.
Updates passed on to AI-INST.
Script checked for errors, and passed.
------------------------------------------------
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
- Vulkan compatible Graphics Card with 8GB+, a graphics card with enough vram to individually load the models you choose (there is no gpu selection, so I advise, solid color desktop and shut down media intensive apps).
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
2. Go to AMD Adrenalin settings, Performance>Metrics>Tracking>, then click (o) on, GPU Memory and System Memory, then on left is, VRam and System Ram, usage, you should calculate how much free that would give you for relevantly, individual and all 3 of the, model files.
3. You should ensure that, for example, if you have 7GB free, then you would want models that are ~5-6GB in size. 
2. Ensure you have Installed the requirements detailed above, for, C++ Build Tools and Python.
3. Download [Qwen-Agent Framework](https://github.com/QwenLM/Qwen-Agent) into a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files directly to that folder.
4. Drop in my scripts for QwenAgent-Interface directly into "Qwen-Agent-0.0.5+" preserving file structure, and relevantly over-writing the "requirements.txt".
5. Install remaining, requirements and libraries, through "QwenAgent-Configure.Bat", and setup the model used and tweak max memory if you feel the need.
6. Run "QwenAgent-Launcher.Bat" to start the session. 

### Notes:
- Go to AMD Adrenalin settings, Performance>Metrics>Tracking>GPU Memory>(o), then on left is GPU Ram usage.
- Developed for and testing on, Matisse CPU with 64GB for 57B models and 8GB Artic Islands GPU for 7b models .

## Credits:
- The producers of...Llama.cpp, Vulkan, Qwen-Agent Framework, Qwen2 series language models...make my project possible.


