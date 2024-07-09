# Cpp-Vulkan-Agi
Project Status: Alpha; Project stopped, other projects priority. Try, AnythingLLM or my llama python chatbot, in the mean-time. there will be complete upload at stage 2. It does not work yet....

### Project Plan
1. The current work is...
- Determine missing elements, that currently may prevent projects from completing, due to not having a more complete set of tools. Find relevant interesting code, determine the optimal implementations, expand upon tools, then integrate those tools including updating promptings. Determine if all the code is implemented correctly relating to tools, are all the tools local and sound, ready for prompt matrix.
- Instead of ".\data\prompts.txt", we should create some kind of prompting "Matrix" in ".\data\prompt_matrix.py", optimally coded, so as for all common required logical prompts are produced to the correctly relating models, in order to carry out tasks correctly with the appropriate relating tools. A second prompt matrix ".\data\prompt_planning.py", to enable the user to communicate with AI-Chat, and for the AI to come out with plans in a specific format, given the example, and some kind of intelligent options for the model to specify, therein, we require it to come out with a list of steps, then when performing each "Current Task", then the AI-CHAT must produce a plan for the step, and then andlyze the plan, to determine the best models to action for each task. There is my plan Or maybe there is some better way to do this, we should research or assess some other scripts, maybe there is some better way its done, I would be open to. being aware of the current tools and what tools are required for each task, in order for tasks to be able to be accomplished. This will require deep analysis of currently implemented code and purposes, so as, to come up with the optimal configuration and operation of a dynamic prompting system for llama.cpp binaries. Functions in ".\scripts\model_interact.py" will logically possibly also require resulting upgrade.
- given the example of the flow of responses, ensure there is some kind of simulated interaction, messages that print in the, "AI-CHAT" and "AI-INST" and "AI-CODE", windows...................finish detail later.... between the AI-Agents during normal operation in the logical proceedings of projects, presented to the user on the interface in the applicable AI-Personalities log panel. This should also require a logical enumeration of workflows for given projects, for example, creating/updating/bugfixing a program, finding out something by researching on the internet, operating system updates. We want to cover all common tasks one is able to do through only text based models. you must enumerate themes of projects and relating interactions and what tasts these projects would contain, and each task will have a theme of AI-Personality, ie AI-CHAT or AI-INST or AI-CODE, they should be assigned to. Projects must be worked through logically. Current Task details and Remaining Tasks and project details, should all each be displayed in their own individual panel. The main thing is to produce the desired results in the backend, while providing a little bit of detail on the frontend so the user knows whats going on roughly in a very-concise short sentence format, typically simply stating actions started/completed. This will require dynamic printed text for each situation relating to the current, options and tools, made, available and aware.
- We do want to take advantage of the features in the framework, ensure to investigate framework examples further, and at the same correct any errors.
- Bugfix scripts to a bug free version that can startup and shutdown.
2. The primary version will have been created and released, now we must...
- optimize and make more dynamic and compacted, the functions, to reclaim some context. 
- investigave correct operation through gradio interface, ensuare ALL features working correctly. Possibly further updates to UI, to improve somehow.
- Ensure the launcher/installer is programmed optimally with regards to consistency in page format and colors used, including returning to launcher from installer.
3. Improve and Expand...
- Option to just use 1 (typically large) model for all purposes, and offload layers onto gpu, then rest in system ram. find how many layers a model has, then devide the number of layers by the size of the model, then use this as a guage as to how many complete layers it is safe to offload to the GPU, given the current load on the GPU, and then load only that number of layers, and the rest to system ram. also subtract something for the "maximum_memory_usage".
- Allow the user to specify non-qwen models, covering llama 3 based moels as well as qwen. Pretty sure the llama.cpp code is mostly there, however we do want to examine the syntax, and ensure we utilize arguments in the command lines optimally and correctly.
- Other Llama.cpp binaries available need researching again, and integrating into the configurator.
- a youtube demonstration video, to gain interest and guide people.
- New name Possibly, QAgent-CppAgi, QwenAgent-CppCore, ??

## Description:
- Currently a project to produce, a, Gradio and LlamaCpp, based Agi, capable of, planning and executing, text/code based projects, to completion. Utilizing the best solutions I can find from research, etc. There are Vulkan versions of llama.cpp, I have done stuff with llama.cpp before, and there are now other projects where people have done Agi with Llama.cpp.

### Features:
1. **Main Script Execution**: Initialization and Launch, reads configuration, and launches the program/gradio interface, the display is then the gradio interface with immediate options for, Settings, Load all Models, Exit Program.
2. **Model Interaction**: There are 3 modes, Chat, Instruct, Code, all of which are loaded so system ram, then when they are required they are individually exclusively loaded to VRam for use with the applicably relating agents.
3. **Agent Management**: Agent Setup: Defines and configures various agent types, and registers tools for tasks like code execution and interpretation. As said, each agent has a relating theme of assigned model, from  Chat, Instruct, Code.
4. **Llama.Cpp Integration**: Direct Model Management: Utilizes the Llama.Cpp, this involves options of Vulkan, which allows for, VRam load monitoring and non-ROCm AMD GPU on Windows. All model processing is done through Vulkan.
5. **Auto Shutdown**: The gradio interface should be displaying the, System RAM and Graphics VRAM, load, this is used by the program to ensure that the CPU/GPU is not over-loaded, if the load hits over "maximum_memory_usage" percent, on either then it will automatically unload all models, to prevent a crash, the user must then, close applications or choose smaller models. 
6. **Real-time Config**: Via clicking on a settings button, the user is able to change useful settings for the program, such as, models choice for, AI-CHAT, AI-INST, AI-CODE, and also, the "maximum_memory_usage" percent through a slider.
7. **Standalone Installer**: Standalone Installer Tool. Users install, requirements and llama.cpp, through this to ".\libraries" subdirectories.
 
### Preview:
- Heres how the Main Page is shaping up...
![Alternative text](https://github.com/wiseman-timelord/QwenCppVulkanAgi/blob/main/media/interface_main.jpg)
- Heres how the Models Page is shaping up...
![Alternative text](https://github.com/wiseman-timelord/QwenCppVulkanAgi/blob/main/media/models_page.jpg)
- Heres how the Memory Page is shaping up...
![Alternative text](https://github.com/wiseman-timelord/QwenCppVulkanAgi/blob/main/media/settings_menu.jpg)
- Standalone Installer for, `requirements.txt` and llama.cpp...
```
========================( Batch Launcher )=======================








                      1. Run Main Program

                     2. Run Installer Tool








----------------------------------------------------------------
Select; Options = 1-2, Exit = X:

```

## Requirements:
- Vulkan compatible Graphics Card with VRam in proportion to the maximum individual size of the 3 models, for example 7B for 8GB cards.
- System Memory 32GB+, or enough system memory to store all 3 of the 7b models you choose AT THE SAME TIME, for fast-load on-demand.
- Python, Developed on [Python 3.12.x](https://www.python.org/downloads/release/python-3120/?ref=upstract.com) Non-WSL, untested on others.
- [Windows 10/11](https://www.ebay.co.uk/b/bn_2683753), but its developed on Windows 10.
- [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) with "Desktop development with C++" installed, so pip can install things like `pyamdgpuinfo`.
- [Requirements.txt](https://github.com/wiseman-timelord/QwenAgent-Interface/blob/main/requirements.txt), mostly from the framework, are installed by the configurator.
- Other libraries, such as [llama.cpp pre-compiled binaries](https://github.com/ggerganov/llama.cpp/releases), are installed by the configurator.


### Instructions:
- Releases are considered non-working, but here are the early instructions...
1. Ensure you are on Windows, and are not using Wsl to run python, unless you know some other method of emulating windows python.
2. Plan your model usage optimally. In Windows 11 you can see Ram/VRam usage in Task Manager, doing this in other versions use Adrenalin Control Panel. You should calculate how much free ram you will have, for, individual models on the VRam and all 3 model files in Ram (no requirement for additional Ram, its just stored there).
3. You should ensure that, for example, if you have 7GB free VRam, then you would want models that are individually ~5-6GB in size (it always needs a little extra). 
2. Ensure you have Installed the requirements detailed above, for, C++ Build Tools and Python.
4. Download and extract my project to some non-system folder, for examle "D:\Programs\GradioCppQwenAgi_v#_##".
5. Install remaining, requirements and libraries, through "GradioCppQwenAgi-Installer.Bat".
6. Run "GradioCppQwenAgi-Launcher.Bat" to start the session. 

### Notes:
- Go to AMD Adrenalin settings, Performance>Metrics>Tracking>GPU Memory>(o), then on left is GPU Ram usage.
- Developed for and testing on, Matisse CPU with 64GB for 57B models and 8GB Artic Islands GPU for 7b models .

## Credits:
- The producers of...Llama.cpp, Vulkan, Auto-GPT, Auto-LLM, Qwen-Agent, llama-cpp-agent, Qwen2 series language models...inspired my project.


