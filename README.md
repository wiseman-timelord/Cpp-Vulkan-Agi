# QAgent-CppAgi
Project Status: Alpha; under development. It does not work yet....

### Current Work
1. Completing the scripts...
- check out the new blueprint for the interface below, try to use only 3 cases for the models roles, and make them more general, this will save on many characters, and may actually work. we should save some chracters from implementing the 3 personalities of AI. 
- given the example of the flow of responses, ensure there is some kind of simulated interaction between the AI-Agents during normal operation in the logical proceedings of projects, presented to the user on the interface in the applicable AI-Personalities log panel. This should also require a logical enumeration of workflows for given projects, for example, creating/updating/bugfixing a program, finding out something by researching on the internet, operating system updates. We want to cover all common tasks one is able to do through only text based models. you must enumerate themes of projects and relating interactions and what tasts these projects would contain, and each task will have a theme of AI-Personality, ie AI-CHAT or AI-INST or AI-CODE, they should be assigned to. Projects must be worked through logically. Current Task details and Remaining Tasks and project details, should all each be displayed in their own individual panel. The main thing is to produce the desired results in the backend, while providing a little bit of detail on the frontend so the user knows whats going on roughly in a very-concise short sentence format, typically simply stating actions started/completed. This will require dynamic printed text for each situation relating to the current, options and tools, made, available and aware.
- Determine if all the code is implemented correctly, by going over qwen-agent tutorials/examples.
- pretty sure the llama.cpp code is mostly there, however we do want to examine the syntax, and ensure we utilize arguments in the command lines optimally and correctly.
- We do want to take advantage of the features in the framework, ensure to investigate framework examples further, and at the same correct any errors.
2. Bugfix scripts to a bug free version that can startup and shutdown.
3. Complete Gradio Interface, does it work with win 10 python 3.12, what can we expect, what are possibilities.
4. investigave correct operation through gradio interface, ensuare all features working correctly.
5. Improve and Expand...
- need to find how many layers a model has, then devide the number of layers by the size of the model, then use this as a guage as to how many complete layers it is safe to offload to the GPU, given the current load on the GPU, and then load only that number of layers, and the rest to system ram. also subtract something for the "maximum_memory_usage".
- agents able to work in parrellel, each having, a copy of the same model.
- Further updates to UI, to integrate all improvements somehow.
- After code context begins to become an issue, then optimize and make more dynamic and compacted, the functions. 
- Other Llama.cpp binaries available need researching again, and integrating into the configurator.
- a youtube demonstration video, to gain interest and guide people.
- New name Possibly, QAgent-CppAgi, QwenAgent-CppCore, ??

## Description:
- Currently a project to produce, a, Gradio and QwenAgent and LlamaCpp, based Agent Manager, capable of managing text or code based projects, to completion, for all that would be useful or interesting. Utilizing the best solutions I can find from research etc. Unfortunately it turned out the AMD on windows is still limited even with DirectML because it requires ROCm. However, as it turns out, there are Vulkan versions of llama.cpp, I have done stuff with llama.cpp before.

### Features:
1. **Main Script Execution**: Initialization and Launch (.\main_launch.py): Reads configuration, and launches the program/gradio interface, the display is then the gradio interface with immediate options for, Settings, Load all Models, Exit Program.
2. **Model Interaction**: There are 3 modes, Chat, Instruct, Code, all of which are loaded so system ram, then when they are required they are individually exclusively loaded to VRam for use with the applicably relating agents.
3. **Gradio Interface**: User Interaction through a multi-panel display, allowing display of, chat, ai actions, project & task details, as well as configuration of settings. 
4. **Agent Management**: Agent Setup (agent_manager.py): Defines and configures various agent types, and registers tools for tasks like code execution and interpretation. As said, each agent has a relating theme of assigned model, from  Chat, Instruct, Code.
5. **Llama.Cpp Integration**: Direct Model Management: Utilizes the Llama.Cpp, this involves options of Vulkan, which allows for, VRam load monitoring and non-ROCm AMD GPU on Windows. All model processing is done through Vulkan.
6. **Auto Shutdown**: The gradio interface should be displaying the, System RAM and Graphics VRAM, load, this is used by the program to ensure that the CPU/GPU is not over-loaded, if the load hits over "maximum_memory_usage" percent, on either then it will automatically unload all models, to prevent a crash, the user must then, close applications or choose smaller models. 
7. **Real-time Config**: Via clicking on a settings button, the user is able to change useful settings for the program, such as, models choice for, AI-CHAT, AI-INST, AI-CODE, and also, the "maximum_memory_usage" percent through a slider.
8. **Standalone Installer**: Standalone Installer Tool (main_install.py). Users install, requirements and llama.cpp, through this to ".\libraries" subdirectories.
 
### Preview:
- This is a purely conceptual blueprint, at this stage.
```
=============== QAgent-CppAgi ===================
=================================================
HUMANOID:
-------------------------------------------------
Log;
I want you to update the files for the interface
we are using.
Please do X to the Y script, then produce relating
required updates for the other relevant code, then
save the file.
When you are done shutdown the interface.
-------------------------------------------------
Input;
...
=================================================
=================================================
AI-CHAT:
-------------------------------------------------
Hello Humanoid, what is it specifically we are doing to the interface of QAgent-CppAgi?
Hmm interesting idea, however this is not completely covered by my training data, and will require, research and a plan and an assessment of the files.
Produced a web-research, data from C is too large, it must be consolidated first. 
Ordering AI-INST to assemble the data. 
New Input, project interrupted, assessing Input.
Noted, after the script is checked and saved as a file, then I will ensure to shutdown appropriately.
Continuing with project: do X to the Y script.
Assessing Data, the research stated B.
Ordering AI-CODE to produce the updates.
Project completed successfully.
Unloading all loaded models.
Shutting down interface in 10 seconds.
=================================================
=================================================
AI-INST:
-------------------------------------------------
New order from AI-CHAT, getting on with order.
Data Assembled, as instructed.
Data Passed on to AI-CHAT.
Functions replaced in script and file saved.
Passing complete script to AI-CODE.
=================================================
=================================================
AI-CODE:
-------------------------------------------------
Analyzing Current Code and relevant information.
Analyzing current code and producing updates.
Updates passed on to AI-INST.
Script checked for errors, and passed.
=================================================
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
2. Plan your model usage optimally. Go to, AMD Adrenalin settings or Open Hardware Monitor or in Windows 11, you should calculate how much free ram you will have, for, individual models on the VRam and all 3 model files in Ram.
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


