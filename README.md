# Computational Models of Social Cognition (CoMoSoCo) - PPL Environment

## Environment Setup

This project uses a virtual environment to manage dependencies. I recommend using a tool like `uv` from Astral for creating and managing these environments.  There are three primary ways to initialize the environment:

1.  **Using Taskfile (Recommended for speed and convenience):** This method leverages `Taskfile` for streamlined setup.
2.  **Manually with `uv` and VS Code:** This approach uses `uv` directly and integrates with VS Code.
3.  **Minimal Dependencies and Cross-Platform:** This method uses only built in tooling and can be used in the widest variety of use-cases, but sacrifices some speed and convenience.

Choose the option that best suits your workflow.

### Option 1: Using Taskfile (Recommended)

This is the recommended method for quickly setting up the development environment. It automates the process using `Taskfile`, a task runner that simplifies common development tasks.

#### Prerequisites

1.  **Install VS Code:** Download and install VS Code from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2.  **Install `uv`:** `uv` is a fast Python package installer and resolver, and can be used to create and manage virtual environments. You can install it using various package managers. For example, using `brew` (macOS):

    ```bash
    brew install uv
    ```

    For other installation methods, see the `uv` documentation: [https://astral.sh/blog/uv/](https://astral.sh/blog/uv/)
3.  **Install `Task`:** `Task` is a task runner/build tool. Install it using `brew` (macOS):

    ```bash
    brew install go-task/tap/go-task
    ```

    For other installation methods, see the `Task` documentation: [https://taskfile.dev/installation/](https://taskfile.dev/installation/)

#### Steps

1.  **Instantiate `uv` Environment:** Run the following command in your terminal in the root directory of this project to create and populate the virtual environment based on instructions in `Taskfile.yml`. The `Taskfile.yml` file automatically uses `uv` under the hood.

    ```bash
    task install
    ```

    This command will:
    *   Create a virtual environment in a `.venv` directory if it doesn't exist.
    *   Install all necessary packages listed in the `requirements.txt` file.
    *   Install the local package in editable mode (changes to the project code are immediately reflected in the virtual environment).

2.  **Open the Project in VS Code:**

    *   Open the project in VS Code by double-clicking the `VSCProject.code-workspace` file (if it exists), or by opening the project folder from within VS Code (File -> Open Folder...).

3.  **Install Recommended Extensions:**

    *   VS Code will likely prompt you to install recommended extensions. Click "Install" to install them. These extensions provide helpful features for Python development. If you don't get prompted, you can manually install them by going to the Extensions tab (Ctrl+Shift+X or Cmd+Shift+X) and searching for the extensions listed in the `.vscode/extensions.json` file.

4.  **Test the Installation:**

    *   Open the `installation-test.ipynb` notebook in VS Code.
    *   In the top-right corner of the notebook, ensure that the kernel is set to the `.venv` virtual environment. If not, click on the kernel selector and choose the correct environment (it should be listed as `.venv` or have a path containing `.venv`).
    *   Run all cells in the notebook (click the "Run All" button or press Shift+Enter in each cell).

If all cells execute without errors, your environment is set up correctly.

### Option 2: Manually with `uv` and VS Code

This method outlines the steps for manually creating and activating the virtual environment using `uv` without relying on `Taskfile`.

#### Prerequisites

1.  **Install VS Code:** Download and install VS Code from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2.  **Install `uv`:** Follow the installation instructions for `uv` provided in Option 1.

#### Steps

1.  **Create the Virtual Environment:**

    ```bash
    uv venv
    ```

    This command creates a new virtual environment in the `.venv` directory.

2.  **Install Packages:**
    ```bash
    uv pip install -r requirements.txt
    ```

    This command installs the project's dependencies into the newly created environment.

3. **Install the local package in editable mode:**
    ```bash
    uv pip install -e .
    ```
    This installs the current package in editable mode. If the code is modified, the changes will immediately be available in the virtual environment.

4.  **Activate the Environment (Optional, but recommended):**
    While not strictly necessary for running code within VS Code (which can handle environment selection automatically), activating the environment in your terminal is useful for running scripts from the command line.
    *   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

    *   **Windows (PowerShell):**

        ```powershell
        .venv\Scripts\Activate.ps1
        ```

    *   **Windows (cmd):**

        ```cmd
        .venv\Scripts\activate.bat
        ```

5.  **Open the Project in VS Code:** Follow the same instructions as in Option 1, steps 2-4. When selecting the kernel in VS Code, choose the `.venv` environment.

### Option 3: Minimal Dependencies and Cross-Platform (venv)

This method prioritizes minimal dependencies and maximum cross-platform compatibility by using only Python's built-in `venv` module. This will allow you to run your code on machines that don't have `uv` or `Taskfile` installed.

#### Prerequisites

1.  **Python 3:** Ensure that Python 3 is installed on your system. You can check by running `python3 --version` or `python --version` in your terminal.

#### Steps

1.  **Create the Virtual Environment:**

    ```bash
    python3 -m venv .venv
    ```

    or, on some systems:

    ```bash
    python -m venv .venv
    ```

    This command creates a new virtual environment in the `.venv` directory using Python's built-in `venv` module.

2.  **Activate the Environment:**

    *   **macOS/Linux:**

        ```bash
        source .venv/bin/activate
        ```

    *   **Windows (PowerShell):**

        ```powershell
        .venv\Scripts\Activate.ps1
        ```

    *   **Windows (cmd):**

        ```cmd
        .venv\Scripts\activate.bat
        ```

3.  **Install Packages:**

    ```bash
    python3 -m pip install -r requirements.txt
    ```
    or, on some systems:

    ```bash
    python -m pip install -r requirements.txt
    ```

    This command installs the project's dependencies into the virtual environment using `pip`.

4. **Install the local package in editable mode:**
    ```bash
    python3 -m pip install -e .
    ```
    or, on some systems:

    ```bash
    python -m pip install -e .
    ```

    This installs the current package in editable mode. If the code is modified, the changes will immediately be available in the virtual environment.

5.  **Using the Environment:**

    *   You can now run Python scripts and notebooks within this environment.
    *   If you're using an IDE like VS Code, you can set the Python interpreter to the `.venv` directory. In VS Code, open the command palette (Ctrl+Shift+P or Cmd+Shift+P) and search for "Python: Select Interpreter". Choose the interpreter path that points to your `.venv` environment.
    *   To test the installation, you can run the `installation-test.ipynb` notebook as described in previous sections. Make sure to select the correct kernel (the `.venv` environment).

## Troubleshooting

*   **Kernel Selection Issues:** If you encounter problems running the `installation-test.ipynb` notebook, double-check that the correct kernel is selected in VS Code.
*   **Dependency Conflicts:** If you face dependency conflicts, try recreating the virtual environment from scratch using the instructions above.
*   **Permission Errors:** If you get permission errors during installation, ensure you have the necessary permissions to write to the project directory and the virtual environment directory.

