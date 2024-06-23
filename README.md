# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
- Configurator needs auto-padding under menu items, on the lines that are displaying the values.
- Configurator, now features install of llama.cpp binaries for, Avx1, Avx2, Avx512, OpenCL, Vulkan. This now requires to be correctly implemented in the scripts.
- It is not possible to run ollama-python without also running a server. There are many new flavors of "Llama.Cpp", VULKAN!! but also, llvm, kompute, msvc, win-rpc, win-sycl, all of which need researching, and then of course there is OpenBlas. Ensure this is figured out and setup corretly for Qwen2.
- We do want to take advantage of the advanced features, for example the advanced context code, code interpreter etc, ensure that these themes of code and associated advantageous code is incorporated correctly into our gradio interface.
- Investigating optimal processing on, gpu and cpu. Q) would AOCL work together with OpenCL, in some kind of hybrid solution, so as to have some kind of enhancement to the OpenCL, seems as its supposed to be slower than DirectML?
- After code context begins to become an issue, then an assessment of the scripts, and where the most lines can be saved, by taking the functions then, optimize and make more dynamic and compacted, so as to generally take less lines, to make the context back to safe level. 
- Ensure project is complete working version, bug free and as intended.
- a youtube demonstration video, to gain interest and guide people.

## Description:
- Qwen-Agent is an agent framework, hence here is my drop in advanced interface for Qwen-Agent. 

### Features:
- Optional Vulkan Llama.Cpp, twice as fast as OpenBlas (the OpenCL version), and it works on nVidia.
- Developed for, Matisse CPU with 64GB and 8GB Artic Islands GPU, aiming for Qwen2 57B GGUF models, with GPU layers. 
- Requirement/Llama.Cpp Install & Startup configuration, through Standalone Configurator Tool for pre-launch.


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

## Instructions:
- Releases are considered non-working, but are produced to save versions of code for later, as idea hopping during alpha. Do not expect the current version to work, its in Alpha stage.
1. Create a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files to the directory you created.
2. Drop in my scripts directly into "Qwen-Agent-0.0.5+" preserving file structure, and over-writing the "requirements.txt".
3. Install the requirements by clicking on "Install_Requirements.Bat", there will be some new library requirements now.
4. Load the model you intend to use in ollama, this possibly can be made easier by running "Load_Qwen2_Model.Bat"
5. Run "QwenAgent-Configurator.Bat" to setup the, model file and graphics mode/card and determine cpu types. other options to come.
6. Run "QwenAgent-LaunchMain.Bat" to start the session. 


