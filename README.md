# Network Monitoring Dashboard 🌐

A modern, responsive web application for monitoring network devices built with Flask and Bootstrap 5.

![Network Dashboard](https://img.shields.io/badge/Status-Active-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-red)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

## ✨ Features

- **⚡ Fast Loading**: Optimized performance with concurrent network scanning
- **📱 Responsive Design**: Modern Bootstrap 5 UI that works on all devices
- **🔍 Network Discovery**: Real-time device scanning with IP, MAC, and hostname detection
- **📊 Live Statistics**: Network stats with device counts and status indicators
- **⚙️ Configurable Settings**: Customizable scan timeouts and auto-refresh options
- **🎨 Modern Interface**: Clean design with smooth animations and hover effects
- **📋 Export Functionality**: Export scan results for analysis
- **🔄 Auto Refresh**: Automatic network scanning at configurable intervals

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/network-monitoring-dashboard.git
   cd network-monitoring-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the dashboard**
   Open your browser and navigate to `http://localhost:5000`

## 🛠️ Usage

### Network Scanning

1. **Default Scan**: The dashboard loads with sample data for instant viewing
2. **Custom Subnet**: Enter a custom network range (e.g., `192.168.1.0/24`) in the subnet field
3. **Scan Network**: Click the "Scan Network" button to discover devices on your network
4. **Refresh**: Use the refresh button or enable auto-refresh for continuous monitoring

### Configuration Options

- **Scan Timeout**: Adjust the timeout for network scans (5-30 seconds)
- **Auto Refresh**: Enable automatic scanning at regular intervals
- **Refresh Interval**: Set the frequency for auto-refresh (30 seconds to 5 minutes)

## 📁 Project Structure

```
network-monitoring-dashboard/
├── app.py                 # Main Flask application with optimized scanning
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Main dashboard template with Bootstrap 5
│   └── static/
│       └── style.css     # Custom CSS with animations and responsive design
└── README.md             # Project documentation
```

## 🔧 Technical Details

### Backend (Flask)
- **Fast Network Scanning**: Uses concurrent ping checks with ThreadPoolExecutor
- **Hostname Resolution**: Automatic reverse DNS lookup for device identification
- **Error Handling**: Graceful fallback to sample data when scanning fails
- **Performance Optimized**: Sample data on GET requests, real scanning on POST

### Frontend (Bootstrap 5)
- **Responsive Grid**: Mobile-first design with responsive breakpoints
- **Interactive Components**: Hover effects, loading states, and smooth animations
- **Modern UI Elements**: Cards, badges, buttons, and form controls
- **Accessibility**: Proper ARIA labels and semantic HTML structure

### Network Scanning Features
- **Concurrent Processing**: Multi-threaded ping checks for faster results
- **Timeout Management**: Configurable timeouts to prevent hanging
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Subnet Support**: Common network ranges (192.168.x.x, 10.x.x.x)

## 🎨 Screenshots

### Main Dashboard
- Clean, modern interface with device table
- Real-time network statistics
- Responsive design for all screen sizes

### Settings Panel
- Configurable scan options
- Auto-refresh controls
- Export and cache management

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Sangam Gupta**
- Created with ❤️ for network monitoring enthusiasts
- Modern, responsive design with optimal performance

## 🙏 Acknowledgments

- Bootstrap 5 for the responsive UI framework
- Flask for the lightweight web framework
- Bootstrap Icons for beautiful iconography
- Python threading for concurrent network operations

---

⭐ **Star this repository if you find it helpful!**
