# 📦 Food Stock Management Assistant

A lightweight Python application designed to simplify food inventory management for users with little or no Excel experience.

## 📋 Overview

This project was inspired by real-world inventory routines observed in a restaurant environment. The goal was to create a simple and intuitive terminal-based solution capable of managing food stock movements while automatically handling data storage in Excel spreadsheets.

Instead of requiring users to manually edit spreadsheets, the system provides an interactive menu interface that makes inventory operations faster, safer, and more accessible.

## ✨ Features

* 📥 Register food stock entries
* 📤 Register food consumption (stock withdrawals)
* 🔍 Search inventory records
* 🗑️ Safely remove records
* 📊 Automatic Excel file creation and updating
* 💾 Real-time data saving
* 🖥️ Interactive terminal menus
* ✅ Input validation
* 🛡️ Error handling and data protection

## 🛠️ Technologies Used

* 🐍 Python
* 🐼 Pandas
* 🎯 InquirerPy
* 📄 OpenPyXL
* 📈 Excel

## 📂 Project Structure

```text
FoodStockManagement/

├── Stock_Management.py
├── food-stock-management-demo.mp4
└── README.md
```

## ⚙️ How It Works

The application stores inventory movements inside an Excel spreadsheet.

Two different inventory flows are tracked:

### 📥 Stock Entry

Used when new food items are purchased or added to inventory.

Information stored:

* ID
* Food Item
* Entry Date
* Quantity

### 📤 Stock Withdrawal

Used when food items are consumed or removed from inventory.

Information stored:

* ID
* Food Item
* Consumption Date
* Quantity

All changes are automatically saved after every operation, reducing the risk of data loss.

## 🚀 Technical Highlights

### 💾 Real-Time Persistence

Data is saved immediately after every modification instead of waiting for program termination.

### ✅ Input Validation

Numeric fields are validated to prevent invalid user input.

### 🛡️ Safe Deletion

Records are removed safely without affecting list iteration.

### 🔧 Error Handling

The application handles common issues such as:

* Missing Excel files
* Invalid keys
* Empty databases
* User input errors

### 🖥️ Interactive User Experience

Built with InquirerPy to provide a clean and user-friendly terminal interface.

## 🔮 Future Improvements

* 🚨 Stock level alerts
* 📊 Consumption reports
* 🗄️ SQLite database integration
* 🎨 Graphical user interface (GUI)
* 📈 Dashboard and analytics
* 👥 Multi-user support

## 💡 Motivation

This project was developed as part of my learning journey in Python and process automation.

The idea originated from observing inventory management activities in a real work environment and creating a solution that could simplify daily operations for users unfamiliar with spreadsheet software.

## 👨‍💻 Author

**Daniel Brum**

⚡ Electrical Engineering Student
🐍 Python Developer
🤖 Process Automation Enthusiast
