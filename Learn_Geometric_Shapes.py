import tkinter as tk
from tkinter import font
import math

class ShapesLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Learn Geometric Shapes!")
        self.root.geometry("800x600")
        self.root.configure(bg='#E8D5F2')
        
        # Title
        title_font = font.Font(family="Arial", size=24, weight="bold")
        title = tk.Label(root, text="🎨 Learn Geometric Shapes! 🎨", 
                        font=title_font, bg='#E8D5F2', fg='#6B2C91')
        title.pack(pady=20)
        
        # Subtitle
        subtitle_font = font.Font(family="Arial", size=14)
        subtitle = tk.Label(root, text="Click on a shape to see it!", 
                           font=subtitle_font, bg='#E8D5F2', fg='#8E44AD')
        subtitle.pack(pady=10)
        
        # Shapes data
        self.shapes = [
            {"name": "Circle", "color": "#FF6B6B"},
            {"name": "Square", "color": "#4ECDC4"},
            {"name": "Triangle", "color": "#FFE66D"},
            {"name": "Rectangle", "color": "#95E1D3"},
            {"name": "Star", "color": "#F38181"},
            {"name": "Hexagon", "color": "#A8E6CF"},
            {"name": "Heart", "color": "#FF8B94"},
            {"name": "Oval", "color": "#DDA15E"}
        ]
        
        # Buttons frame
        buttons_frame = tk.Frame(root, bg='#E8D5F2')
        buttons_frame.pack(pady=20)
        
        # Create buttons in grid
        button_font = font.Font(family="Arial", size=12, weight="bold")
        for i, shape in enumerate(self.shapes):
            row = i // 4
            col = i % 4
            btn = tk.Button(buttons_frame, text=shape["name"], 
                          font=button_font, bg=shape["color"], 
                          fg='white', width=12, height=2,
                          command=lambda s=shape: self.show_shape(s),
                          cursor="hand2", relief=tk.RAISED, bd=3)
            btn.grid(row=row, column=col, padx=10, pady=10)
        
        # Canvas for drawing shapes
        self.canvas_frame = tk.Frame(root, bg='white', relief=tk.RIDGE, bd=3)
        self.canvas_frame.pack(pady=20, padx=50, fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, bg='white', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.shape_label = tk.Label(self.canvas_frame, text="", 
                                    font=font.Font(family="Arial", size=16, weight="bold"),
                                    bg='white')
        self.shape_label.pack(pady=10)
    
    def show_shape(self, shape):
        # Clear canvas
        self.canvas.delete("all")
        
        # Update label
        self.shape_label.config(text=f"This is a {shape['name']}!", fg=shape['color'])
        
        # Get canvas dimensions
        self.canvas.update()
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        cx, cy = w // 2, h // 2
        
        # Draw the shape
        color = shape['color']
        
        if shape['name'] == "Circle":
            r = min(w, h) // 3
            self.canvas.create_oval(cx-r, cy-r, cx+r, cy+r, 
                                   fill=color, outline='black', width=3)
        
        elif shape['name'] == "Square":
            s = min(w, h) // 3
            self.canvas.create_rectangle(cx-s, cy-s, cx+s, cy+s, 
                                        fill=color, outline='black', width=3)
        
        elif shape['name'] == "Triangle":
            s = min(w, h) // 2.5
            points = [cx, cy-s, cx-s, cy+s, cx+s, cy+s]
            self.canvas.create_polygon(points, fill=color, outline='black', width=3)
        
        elif shape['name'] == "Rectangle":
            w_rect = min(w, h) // 2.5
            h_rect = min(w, h) // 4
            self.canvas.create_rectangle(cx-w_rect, cy-h_rect, cx+w_rect, cy+h_rect, 
                                        fill=color, outline='black', width=3)
        
        elif shape['name'] == "Star":
            self.draw_star(cx, cy, min(w, h) // 3, color)
        
        elif shape['name'] == "Hexagon":
            self.draw_hexagon(cx, cy, min(w, h) // 4, color)
        
        elif shape['name'] == "Heart":
            self.draw_heart(cx, cy, min(w, h) // 3, color)
        
        elif shape['name'] == "Oval":
            rx = min(w, h) // 2.5
            ry = min(w, h) // 4
            self.canvas.create_oval(cx-rx, cy-ry, cx+rx, cy+ry, 
                                   fill=color, outline='black', width=3)
    
    def draw_star(self, cx, cy, size, color):
        points = []
        for i in range(10):
            angle = math.pi / 2 + (2 * math.pi * i / 10)
            r = size if i % 2 == 0 else size / 2.5
            x = cx + r * math.cos(angle)
            y = cy - r * math.sin(angle)
            points.extend([x, y])
        self.canvas.create_polygon(points, fill=color, outline='black', width=3)
    
    def draw_hexagon(self, cx, cy, size, color):
        points = []
        for i in range(6):
            angle = math.pi / 6 + (2 * math.pi * i / 6)
            x = cx + size * math.cos(angle)
            y = cy + size * math.sin(angle)
            points.extend([x, y])
        self.canvas.create_polygon(points, fill=color, outline='black', width=3)
    
    def draw_heart(self, cx, cy, size, color):
        points = []
        for t in range(0, 360, 5):
            rad = math.radians(t)
            x = 16 * math.sin(rad) ** 3
            y = -(13 * math.cos(rad) - 5 * math.cos(2*rad) - 
                  2 * math.cos(3*rad) - math.cos(4*rad))
            points.extend([cx + x * size / 17, cy + y * size / 17])
        self.canvas.create_polygon(points, fill=color, outline='black', width=3)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ShapesLearningApp(root)
    root.mainloop()