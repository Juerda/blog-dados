// Pie Chart and CSV Export Functionality

class PieChart {
    constructor(canvasId, data, colors) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            console.warn(`Canvas with ID ${canvasId} not found`);
            return;
        }
        this.ctx = this.canvas.getContext('2d');
        this.data = data;
        this.colors = colors;
        
        // Set canvas resolution
        this.canvas.width = this.canvas.offsetWidth;
        this.canvas.height = this.canvas.offsetHeight;
        
        this.centerX = this.canvas.width / 2;
        this.centerY = this.canvas.height / 2;
        this.radius = Math.min(this.canvas.width, this.canvas.height) / 2 - 20;
        
        this.draw();
    }

    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        const total = this.data.reduce((sum, item) => sum + item.value, 0);
        let currentAngle = -Math.PI / 2;

        this.data.forEach((item, index) => {
            const sliceAngle = (item.value / total) * 2 * Math.PI;
            
            // Draw slice with shadow
            this.ctx.save();
            this.ctx.shadowColor = 'rgba(0,0,0,0.2)';
            this.ctx.shadowBlur = 10;
            this.ctx.shadowOffsetX = 0;
            this.ctx.shadowOffsetY = 3;
            
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, this.radius, currentAngle, currentAngle + sliceAngle);
            this.ctx.lineTo(this.centerX, this.centerY);
            this.ctx.fillStyle = this.colors[index];
            this.ctx.fill();
            
            this.ctx.restore();
            
            // Draw border
            this.ctx.strokeStyle = '#fff';
            this.ctx.lineWidth = 2;
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, this.radius, currentAngle, currentAngle + sliceAngle);
            this.ctx.lineTo(this.centerX, this.centerY);
            this.ctx.stroke();

            // Draw label with percentage
            const labelAngle = currentAngle + sliceAngle / 2;
            const labelX = this.centerX + Math.cos(labelAngle) * (this.radius * 0.65);
            const labelY = this.centerY + Math.sin(labelAngle) * (this.radius * 0.65);

            this.ctx.fillStyle = '#ffffff';
            this.ctx.font = 'bold 16px Arial, sans-serif';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            
            const percentage = item.percentage || Math.round((item.value / total) * 100);
            this.ctx.fillText(percentage + '%', labelX, labelY);

            currentAngle += sliceAngle;
        });
    }

    getData() {
        return this.data;
    }
}

// CSV Export Function
function downloadCSV(data, filename, title = '') {
    let csv = '';
    
    if (title) {
        csv += title + '\n\n';
    }

    // Headers
    if (data.length > 0) {
        const headers = Object.keys(data[0]);
        csv += headers.join(',') + '\n';

        // Rows
        data.forEach(row => {
            const values = headers.map(header => {
                const value = row[header];
                // Escape quotes and wrap in quotes if contains comma
                if (typeof value === 'string' && value.includes(',')) {
                    return '"' + value.replace(/"/g, '""') + '"';
                }
                return value;
            });
            csv += values.join(',') + '\n';
        });
    }

    // Create blob and download
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement('a');
    const url = URL.createObjectURL(blob);
    
    link.setAttribute('href', url);
    link.setAttribute('download', filename);
    link.style.visibility = 'hidden';
    
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    
    // Clean up
    URL.revokeObjectURL(url);
}

// Initialize pie charts when page loads
function initPieCharts() {
    // Find all CSV export buttons and attach handlers
    const csvButtons = document.querySelectorAll('.csv-export-button');
    csvButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('data-target');
            const filename = this.getAttribute('data-filename') || 'dados.csv';
            const title = this.getAttribute('data-title') || '';
            
            if (targetId) {
                const chart = window.pieCharts && window.pieCharts[targetId];
                if (chart && typeof chart.getData === 'function') {
                    const data = chart.getData();
                    downloadCSV(data, filename, title);
                } else {
                    console.warn(`Chart ${targetId} not found or has no getData method`);
                }
            }
        });
    });
    
    // Redraw charts on window resize
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function() {
            const canvases = document.querySelectorAll('canvas');
            canvases.forEach(canvas => {
                const oldWidth = canvas.width;
                const oldHeight = canvas.height;
                canvas.width = canvas.offsetWidth;
                canvas.height = canvas.offsetHeight;
            });
        }, 250);
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPieCharts);
} else {
    initPieCharts();
}

// Store pie charts globally for access
window.pieCharts = window.pieCharts || {};
