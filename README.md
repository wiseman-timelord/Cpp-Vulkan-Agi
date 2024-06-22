# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
- Implement option 1 on configurator menu to be "1. Install Requirments", to install the requirements, then pause, then return to menu. Also remove "Install_Requirements.Bat".
- Using ollama-python for model handling, in order to take a more direct approach to model handling. Ensure this is setup corretly for Qwen2.
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
- The project will be optimized for 64GB ram, hence developed on the model Qwen2-56B-6Bit-GGUF. 
- Configuration of models through Standalone Configrator Tool for pre-launch json configuration.
- Will be tailoed towards AMD, Artic Islands GPU and Matisse CPU, compatible hardware.

### Preview:
- Standalone Configurator (needs updating for new configuration of functions)...
```
Configurator Main Menu

1. Model Options
(CurrentModel: None)
2. Processor Options
(CurrentProcessor: None)
3. GPU Memory Usage
(CurrentUsage: 50%)

----------------------
Selection; Choose Options = 1-3, Exit Program = X:

```

## Instructions:
- Releases are considered non-working, but are produced to save versions of code for later, as idea hopping during alpha. Do not expect the current version to work, its in Alpha stage.
1. Create a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files to the directory you created.
2. Drop in my scripts directly into "Qwen-Agent-0.0.5+" preserving file structure, and over-writing the "requirements.txt".
3. Install the requirements by clicking on "Install_Requirements.Bat", there will be some new library requirements now.
4. Load the model you intend to use in ollama, this possibly can be made easier by running "Load_Qwen2_Model.Bat"
5. Run "QwenAgent-Configurator.Bat" to setup the, model file and graphics mode/card and determine cpu types. other options to come.
6. Run "QwenAgent-LaunchMain.Bat" to start the session. 


