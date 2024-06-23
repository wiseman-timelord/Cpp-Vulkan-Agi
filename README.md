# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
1. There are placeholders in main_launch in the main function, this will require to be completed...
- Placeholder to show the initial model response
- Proceed with setting up Gradio and other components
2. Complete script to bug free version that can startup and shutdown.
3. Complete Gradio Interface, does it work with win 10 python 3.12, what can we expect, what are possibilities.
4. We do want to take advantage of the features in the framework, ensure to investigate framework further.
5. Correct, Improve and Expand...
- After code context begins to become an issue, then optimize and make more dynamic and compacted, the functions. 
- Other Llama.cpp binaries available need researching again, and integrating into the configurator.
- a youtube demonstration video, to gain interest and guide people.

## Description:
- Qwen-Agent is an agent framework, hence here is my drop in advanced interface for Qwen-Agent. 

### Features:
- No requirement of, Ollama or LMStudio, models are accessed through llama.cpp pre-compiled binaries.
- Optional Vulkan, reportedly twice as fast as OpenCL, and it works on nVidia, otherwise its all AMD. 
- Standalone Configurator Tool, for pre-launch, Install & Setup, through, pip and webrequest and github
 
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
- Llama.Cpp pre-compiled binaries, this is installed by the configurator.
- Requirements.txt, this is installed by the configurator.
- Python Developed on Python 3.12.4, untested on others.
- Windows Non-WSL, most will work, but its developed on Windows 10.

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


