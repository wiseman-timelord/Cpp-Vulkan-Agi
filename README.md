# QwenAgent-Interface
Project Status: Alpha; under development. To produce, some awesome interface for the Qwen-Agent framework....

### Current Work
- Removing, nVidia and Intel, support, steamlining as much as possible, for completion.
- Now there is less code for menus and handling, Other things can be done.
- Determining best solutions to AMD, GPU and CPU, whatever is best for, Artic Islands level GPU and Matisse level CPU.
- Still to make the project complete working version, bug free and as intended.
- Investigating processing on, gpu and cpu, while load model on system ram.
- Are the new AMD AOCL, able to be better taken advantage somehow in the scripts, would this work seamlessly better with, AOCL processor and opencl for the graphics, and so produce better combined processing? or even just better than directml for the cpu?


## Description:
- Qwen-Agent is an agent framework, hence here is my drop in interface for Qwen-Agent. 

### Features:
- Pre-gradio interface for configuration of models through dynamic menu, before main.
- The project will be progrogrammed for, AMD/nVidia Gpu via Directml and Intel/Amd, support.
- The project will be optimized for 64GB ram and  hence developed on the model Qwen2-56B-6Bit-GGUF. 
- Code will be tailored towards technology level of AMD4/DirectX_12 level hardware.

### Preview:
- Standalone Configurator...
```
Config Main Menu

1. Model Options
(CurrentModel: None)
2. Processor Options
(CurrentProcessor: None)

----------------------
Selection; Choose Options = 1-2, Exit Program = X:
```

## Instructions:
- Do not expect the current version to work, its in Alpha stage.
1. Create a folder in a suitable location for example "Qwen-Agent-0.0.5+", copy/clone the files to the directory you created.
2. Drop in my scripts directly into "Qwen-Agent-0.0.5+" preserving file structure, and over-writing the "requirements.txt".
3. Install the requirements by clicking on "Install_Requirements.Bat", there will be some new library requirements now.
4. Load the model you intend to use in ollama, this possibly can be made easier by running "Load_Qwen2_Model.Bat"
5. Run "QwenAgent-Configurator.Bat" to setup the, model file and graphics mode/card and determine cpu types. other options to come.
6. Run "QwenAgent-LaunchMain.Bat" to start the session. 


