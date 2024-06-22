# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
- Implement option 1 on configurator menu to be "1. Install Requirments", to install the requirements, then pause, then return to menu. Also remove "Install_Requirements.Bat".
- Using ollama-python for model handling, in order to take a more direct approach to model handling. Ensure this is setup corretly for Qwen2. Remove "Load_Qwen2_Model.Bat" when done.
- We do want to take advantage of the advanced features, for example the advanced context code, code interpreter etc, ensure that these themes of code and associated advantageous code is incorporated correctly into our gradio interface.
- Determining best solutions to AMD, GPU and CPU, whatever is best for, Artic Islands level GPU and Matisse level CPU.
- Investigating optimal processing on, gpu and cpu, are the new AMD AOCL, able to be better taken advantage somehow in the scripts, would this work seamlessly better with, AOCL processor and opencl/AOCL for the graphics, and so produce better combined processing?
- After code context begins to become an issue, then an assessment of the scripts, and where the most lines can be saved, by taking the functions then, optimize and make more dynamic and compacted, so as to generally take less lines, to make the context back to safe level. 
- Ensure project is complete working version, bug free and as intended.
- Its AMD only, but will possibly feature intel/nvidia later, at some point after completion.

## Description:
- Qwen-Agent is an agent framework, hence here is my drop in advanced interface for Qwen-Agent. 

### Features:
- The project will be aiming towards AMD Gpu via choice of, Directml or OpenCL.
- Developed for System with 64GB System and 8GB Graphics, hence, Qwen2 GGUF models, 56B and 7B. 
- Startup configuration through Standalone Configurator Tool for pre-launch json configuration.
- Will be tailoed towards AMD, Artic Islands GPU and Matisse CPU, compatible hardware.

### Preview:
- Dunno how I am going to show the main program, its a graphical interface. Probably will have to resurrect my website, and get some kind of auto-login thing working so it dont timeout again...
```
===== Some Impressive Bot Management =======

--------------------------------------------
ROBOT1:
I am a robot, my prime directive is to go to the shops,
and buy 10 fags.
-----------------------------------------
ROBOT2:
I am designing new hair for ROBOT1.


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


