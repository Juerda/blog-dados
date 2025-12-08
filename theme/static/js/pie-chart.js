// Pie Chart and CSV Export Functionality

class PieChart {
    constructor(canvasId, data, colors) {
        this.canvas = document.getElementById(canvasId);
        this.ctx = this.canvas.getContext('2d');
        this.data = data;
        this.colors = colors;
        this.centerX = this.canvas.width / 2;
        this.centerY = this.canvas.height / 2;
        this.radius = Math.min(this.canvas.width, this.canvas.height) / 2 - 10;
        this.draw();
    }

    draw() {
        const total = this.data.reduce((sum, item) => sum + item.value, 0);
        let currentAngle = -Math.PI / 2;

        this.data.forEach((item, index) => {
            const sliceAngle = (item.value / total) * 2 * Math.PI;
            
            // Draw slice
            this.ctx.beginPath();
            this.ctx.arc(this.centerX, this.centerY, this.radius, currentAngle, currentAngle + sliceAngle);
            this.ctx.lineTo(this.centerX, this.centerY);
            this.ctx.fillStyle = this.colors[index];
            this.ctx.fill();
            this.ctx.strokeStyle = '#fff';
            this.ctx.lineWidth = 2;
            this.ctx.stroke();

            // Draw label
            const labelAngle = currentAngle + sliceAngle / 2;
            const labelX = this.centerX + Math.cos(labelAngle) * (this.radius * 0.7);
            const labelY = this.centerY + Math.sin(labelAngle) * (this.radius * 0.7);

            this.ctx.fillStyle = '#fff';
            this.ctx.font = 'bold 14px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.textBaseline = 'middle';
            this.ctx.fillText(item.percentage + '%', labelX, labelY);

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
}

// Initialize pie charts when page loads
document.addEventListener('DOMContentLoaded', function() {
    // Find all CSV export buttons and attach handlers
    const csvButtons = document.querySelectorAll('.csv-export-button');
    csvButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const filename = this.getAttribute('data-filename') || 'dados.csv';
            const title = this.getAttribute('data-title') || '';
            
            if (targetId) {
                const chart = window.pieCharts && window.pieCharts[targetId];
                if (chart) {
                    downloadCSV(chart.getData(), filename, title);
                }
            }
        });
    });
});

// Store pie charts globally for access
window.pieCharts = window.pieCharts || {};
