# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
- Working further into Configurator, now intended to install and configure, Avx1, Avx2, Avx512, OpenCL, Vulkan; All flavors of AMD.
- It is not possible to run ollama-python without also running a server. There are many new flavors of "Llama.Cpp", VULKAN!! but also, llvm, kompute, msvc, win-rpc, win-sycl, all of which need researching, and then of course there is OpenBlas. Ensure this is figured out and setup corretly for Qwen2.
- We do want to take advantage of the advanced features, for example the advanced context code, code interpreter etc, ensure that these themes of code and associated advantageous code is incorporated correctly into our gradio interface.
- Investigating optimal processing on, gpu and cpu. Q) would AOCL work together with OpenCL, in some kind of hybrid solution, so as to have some kind of enhancement to the OpenCL, seems as its supposed to be slower than DirectML?
- After code context begins to become an issue, then an assessment of the scripts, and where the most lines can be saved, by taking the functions then, optimize and make more dynamic and compacted, so as to generally take less lines, to make the context back to safe level. 
- Ensure project is complete working version, bug free and as intended.
- Its AMD only, but will possibly feature intel/nvidia later, at some point after completion.
- a youtube demonstration video, to gain interest and guide people.

## Description:
- Qwen-Agent is an agent framework, hence here is my drop in advanced interface for Qwen-Agent. 

### Features:
- The project will be aiming towards AMD Gpu via choice of, Directml or OpenCL.
- Developed for System with 64GB System and 8GB Graphics, hence, Qwen2 GGUF models, 56B and 7B. 
- Startup configuration through Standalone Configurator Tool for pre-launch json configuration.
- Will be tailoed towards AMD, Artic Islands GPU and Matisse CPU, compatible hardware.

### Preview:
- Dunno how I am going to show the main program, possibly get a image to text converter or resurrect my webspace, here is improvised content to demonstrate the concept...
```
===== Some Impressive Bot Management =======

HUMAN:
I neez some fags, make a plan, and get me some, so I can
sit in my chair, and finish my project without thinking
about how life is passing by.
--------------------------------------------
ROBOT1:
I am a robot, my prime directive is to go to the shops,
and buy 10 fags, but first I must aquire a disguise.
-----------------------------------------
ROBOT2:
I am designing new hair and beard for ROBOT1, so it can blend-in
with the other humans.
----------------------------------------
ROBOT3:
I am making backup plan for growing tobacco, in case
there are no fags at the shop.


```
- Standalone Configurator...
```
=================( Main Configurator Menu )==============


1. Install Requirements
(Last Updated: Never)

2. Model Location
(CurrentModel: ...4B-GGUF\Qwen2-57B-A14B.Q6_K.gguf)

3. Graphics Method
(CurrentMethod: DirectML)

4. GPU Memory Usage
(CurrentUsage: 66%)


---------------------------------------------------------
Selection; Choose Options = 1-4, Exit & Save = X:

```

## Instructions:
- Releases are considered non-working, but are produced to save versions of code for later, as idea hopping during alpha. Do not expect the current version to work, its in Alpha stage.
1. Create a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files to the directory you created.
2. Drop in my scripts directly into "Qwen-Agent-0.0.5+" preserving file structure, and over-writing the "requirements.txt".
3. Install the requirements by clicking on "Install_Requirements.Bat", there will be some new library requirements now.
4. Load the model you intend to use in ollama, this possibly can be made easier by running "Load_Qwen2_Model.Bat"
5. Run "QwenAgent-Configurator.Bat" to setup the, model file and graphics mode/card and determine cpu types. other options to come.
6. Run "QwenAgent-LaunchMain.Bat" to start the session. 


