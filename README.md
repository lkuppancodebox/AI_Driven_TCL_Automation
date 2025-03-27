# AI-Driven TCL Script Automation

## 📌 Overview
This project automates **TCL script generation** using AI (Google Gemini) based on a structured test plan and function libraries. It reads a test plan, converts it into a **prompt**, and generates an executable **TCL script** (that fits to a particular TCL Framework) automatically, reducing manual effort and errors.

## 🚀 Features
- **AI-Powered Automation**: Uses Google Gemini API to generate TCL scripts.
- **Test Plan to Code**: Converts a text-based test plan into a working TCL script.
- **Error Handling**: Automatically filters unwanted content from AI responses.
- **File Output**: Saves the generated script in Google Drive for easy access.

## 📂 Project Structure
```
├── ai_driven_automation.ipynb  # Main script
├── training_data_set/
│   ├── api_key.txt  # API key file (hidden for security)
│   ├── Automation_testplan.txt  # Test plan input
│   ├── gen_prompt.py  # Generates AI prompt
├── Output/
│   ├── generated_script.tcl  # AI-generated TCL script
```

## 🛠 Installation & Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/ai-tcl-automation.git
   cd ai-tcl-automation
   ```
2. Install dependencies:
   ```bash
   pip install google-generativeai pandas
   ```
3. Set up **Google Gemini API Key**:
   - Save your API key inside `training_data_set/api_key.txt`.

## 📌 Usage
1. **Authenticate & Initialize Model**
   ```python
   model = Authenticate_model()
   ```
2. **Read Test Plan & Generate Prompt**
   ```python
   fid = open("training_data_set/Automation_testplan.txt", "r")
   query = fid.read()
   fid.close()
   prompt = generate_prompt(query, tclLib2Json())
   ```
3. **Generate TCL Script**
   ```python
   response = Genereate_exos_tcl_automation(model, prompt)
   ```
4. **Save Generated Script**
   ```python
   with open("Output/generated_script.tcl", "w") as file:
       file.write(response)
   ```
5. **Check Output**
   ```bash
   ls Output/
   ```

## 📈 Benefits
✅ **Reduces script development time** from days to minutes.
✅ **Eliminates manual errors** with AI-driven automation.
✅ **Empowers non-technical users** to generate TCL scripts easily.

## 🤖 Future Enhancements
- Support for **multiple AI models** (Gemini, OpenAI, etc.).
- Web-based UI for easy script generation.
- Enhanced error handling & debugging features.

---
📌 **Author**: [Lakshmanan Kuppan]  
📌 **License**: MIT  
📌 **Contributions**: Open to pull requests & feature suggestions! 🚀

