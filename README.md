# QwenAgent-Interface
Project Status: Alpha; under development. It does not work yet....

### Current Work
1. Completing the scripts...
- Determine if all the code is implemented correctly, by going over qwen-agent tutorials/examples.
- pretty sure the llama.cpp code is mostly there, however we do want to examine the syntax, and ensure we utilize arguments in the command lines optimally and correctly.
- We do want to take advantage of the features in the framework, ensure to investigate framework examples further.
- Possibly We need to ensure to utilize 
2. Bugfix scripts to a bug free version that can startup and shutdown.
3. Complete Gradio Interface, does it work with win 10 python 3.12, what can we expect, what are possibilities.
4. investigave correct operation through gradio interface, ensuare all features working correctly.
5. Improve and Expand...
- agents able to work in parrellel, each having, a copy of the same model.
- Multi-model, running multiple models each with a share of the threads, multi-agent could then utilize different models.
- Further updates to UI, to integrate all improvements somehow.
- After code context begins to become an issue, then optimize and make more dynamic and compacted, the functions. 
- Other Llama.cpp binaries available need researching again, and integrating into the configurator.
- a youtube demonstration video, to gain interest and guide people.

## Description:
- Currently a project to produce, a, Gradio and QwenAgent and LlamaCpp, based Agent Manager, capable of managing text or code based projects, to completion, for all that would be useful or interesting. Utilizing the best solutions I can find from research etc. Unfortunately it turns out the AMD on windows is still limited even with DirectML, because that only works on certain AMD hardware with windows. So we are reverting to llama.cpp, and inadvertantly finding llama.cpp does now infact feature vulkan, and has been for a while, this saves the project for me, but also makes me wonder why ollama is not using this, as it uses llamacpp binaries too doesnt it?

### Features:
- No requirement of, Ollama or LMStudio, models are accessed through llama.cpp pre-compiled binaries.
- Optional Vulkan, reportedly twice as fast as OpenCL, and it works on nVidia, otherwise its all AMD. 
- Standalone Configurator Tool, for pre-launch, Install & Setup, through, pip and webrequest and github.
- Monitoring of system memory usage with auto-unload model, to ensure computer is not over-loaded.
 
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
- Standalone Configurator looks the part now...
```
=====================( Main Configurator Menu )==================


                     1. Install Requirements
                          (2024/06/23)

                    2. Install Llama Binaries
                             (b3197)

                       3. Processing Method
                (llama-b3197-bin-win-vulkan-x64)

                       4. GPU Memory Usage
                              (80%)

                        5. GGUF Model Used
                  (dolphin-2.9.2-qwen2-7b.Q6_K)


-----------------------------------------------------------------
Selection; Choose Options = 1-5, Exit & Save = X:
```

## Requirements:
- Python, Developed on [Python 3.12.x](https://www.python.org/downloads/release/python-3120/?ref=upstract.com) Non-WSL, untested on others.
- [Windows](https://www.ebay.co.uk/b/bn_2683753), most will work, but its developed on Windows 10.
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with "Desktop development with C++" installed, so pip can install things like `pyamdgpuinfo`.
- Requirements.txt, mostly from the framework, are installed by the configurator.
- Other libraries, such as llama.cpp, are installed by the configurator.


### Instructions:
- Releases are considered non-working, but are produced to save versions of code for later, as idea hopping during alpha. Do not expect the current version to work, its in Alpha stage.
1. Create a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files to the directory you created.
2. Drop in my scripts directly into "Qwen-Agent-0.0.5+" preserving file structure, and over-writing the "requirements.txt".
3. Install the requirements by clicking on "Install_Requirements.Bat", there will be some new library requirements now.
4. Load the model you intend to use in ollama, this possibly can be made easier by running "Load_Qwen2_Model.Bat"
5. Run "QwenAgent-Configurator.Bat" to setup the, model file and graphics mode/card and determine cpu types. other options to come.
6. Run "QwenAgent-LaunchMain.Bat" to start the session. 

### Notes:
- Developed for and testing on, Matisse CPU with 64GB for 57B models and 8GB Artic Islands GPU for 7b models .

## Credits:
- The producers of...Llama.cpp, Vulkan, Qwen-Agent Framework, Qwen2 series language models...make my project possible.


