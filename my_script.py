from flask import Flask, request

app = Flask(__name__)

# Complete custom database with Indian meals and chocolaty desserts!
meal_plan = {
    "Monday": {
        "Breakfast": ["Idli with Coconut Chutney", "Poha with Peas", "Aloo Paratha"],
        "Lunch": ["Chicken Biryani with Raita", "Dal Tadka with Rice", "Paneer Butter Masala & Roti"],
        "Snacks": ["Warm Tiramisu Cup", "Chocolate Lava Cake"],
        "Dinner": ["Butter Chicken with Naan", "Mixed Veg Korma & Rice"]
    },
    "Tuesday": {
        "Breakfast": ["Masala Omelette & Toast", "Upma", "Chole Bhature"],
        "Lunch": ["Fish Curry with Rice", "Rajma Chawal", "Veg Pulao"],
        "Snacks": ["Crispy Chocolate Kunafa", "Fudgy Chocolate Brownie"],
        "Dinner": ["Mutton Rogan Josh with Roti", "Palak Paneer & Rice"]
    },
    "Wednesday": {
        "Breakfast": ["Earthy Moong Dal Cheela", "Methi Thepla", "Bread Upma"],
        "Lunch": ["Egg Curry with Steamed Rice", "Chole Chawal", "Bhindi Masala & Roti"],
        "Snacks": ["Chocolate Truffle Slice", "Nutella Stuffed Crepe"],
        "Dinner": ["Tandoori Chicken Tikka", "Dal Makhani with Laccha Paratha"]
    },
    "Thursday": {
        "Breakfast": ["Crispy Plain Dosa with Sambar", "Vada Pav", "Suji Halwa"],
        "Lunch": ["Chicken Korma with Pulao", "Kadhi Pakora with Rice", "Aloo Gobi & Paratha"],
        "Snacks": ["White Chocolate Tiramisu", "Chocolate Mousse"],
        "Dinner": ["Chicken Seekh Kebab", "Jeera Rice with Yellow Dal"]
    },
    "Friday": {
        "Breakfast": ["Puri Bhaji", "Spiced Bread Roll", "Egg Bhurji with Pav"],
        "Lunch": ["Hyderabadi Chicken Biryani", "Sambhar Rice", "Malai Kofta & Naan"],
        "Snacks": ["Authentic Sweet Cheese Kunafa", "Chocolate Eclairs"],
        "Dinner": ["Grilled Fish Masala", "Mutter Paneer with Roti"]
    },
    "Saturday": {
        "Breakfast": ["Misal Pav", "Sabudana Khichdi", "Cheese Uttapam"],
        "Lunch": ["Mutton Biryani", "Lemon Rice with Papad", "Shahi Paneer & Rumali Roti"],
        "Snacks": ["Dark Chocolate Fondue", "Triple Chocolate Cake Slice"],
        "Dinner": ["Chicken Shawarma Wrap", "Veg Jalfrezi with Naan"]
    },
    "Sunday": {
        "Breakfast": ["Bedmi Puri with Aloo Sabzi", "Kachori", "Masala Dosa"],
        "Lunch": ["Grand Family Chicken Feast", "Veg Dum Biryani", "Dal Baati Churma"],
        "Snacks": ["Classic Coffee Tiramisu", "Warm Chocolate Soufflé"],
        "Dinner": ["Leftover Special Platter", "Egg Hakka Noodles & Chilli Chicken"]
    }
}

@app.route('/')
def home():
    selected_day = request.args.get('day', 'Monday')
    selected_meal = request.args.get('meal', 'Breakfast')
    
    # Custom background color gradients for each individual meal box type
    meal_gradients = {
        "Breakfast": "linear-gradient(135deg, #ffffff 0%, #fffde7 100%)",
        "Lunch": "linear-gradient(135deg, #ffffff 0%, #f1f8e9 100%)",
        "Snacks": "linear-gradient(135deg, #ffffff 0%, #fce4ec 100%)",
        "Dinner": "linear-gradient(135deg, #ffffff 0%, #fff3e0 100%)"
    }
    
    meal_borders = {
        "Breakfast": "#fbc02d",
        "Lunch": "#7cb342",
        "Snacks": "#e91e63",
        "Dinner": "#fb8c00"
    }

    chosen_card_bg = meal_gradients[selected_meal]
    chosen_border = meal_borders[selected_meal]
    
    html = f"""
    <style>
        body {{
            background-color: #f7f1e3;
            background-image: 
                linear-gradient(90deg, rgba(218, 165, 32, 0.08) 50%, transparent 50%),
                linear-gradient(rgba(218, 165, 32, 0.08) 50%, transparent 50%);
            background-size: 40px 40px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 40px 20px;
            color: #333;
        }}
        
        /* This upgrades the main white box to a beautiful light multi-color pastel rainbow gradient */
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: linear-gradient(135deg, #ffeffe 0%, #eef5ff 50%, #e8fcf0 100%);
            padding: 40px;
            border-radius: 24px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.08);
            border: 1px solid rgba(255, 255, 255, 0.6);
        }}
        h1 {{
            color: #000000;
            text-align: center;
            font-size: 2.6em;
            margin-bottom: 5px;
            font-weight: 800;
        }}
        .subtitle {{
            text-align: center;
            color: #2c3e50;
            font-weight: 600;
            margin-bottom: 35px;
            font-size: 1.1em;
        }}
        .tabs {{
            display: flex;
            justify-content: space-between;
            margin-bottom: 25px;
            background: rgba(0, 0, 0, 0.04);
            padding: 6px;
            border-radius: 14px;
        }}
        .tab-btn {{
            flex: 1;
            text-align: center;
            padding: 12px 5px;
            text-decoration: none;
            color: #2c3e50;
            font-weight: 700;
            border-radius: 10px;
            margin: 0 3px;
            transition: all 0.2s ease-in-out;
        }}
        .tab-btn:hover {{ background: rgba(0, 0, 0, 0.05); color: #000; }}
        .active-day {{ background: #000000 !important; color: white !important; }}
        
        .meal-menu {{
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 35px;
        }}
        .meal-btn {{
            padding: 12px 28px;
            text-decoration: none;
            background: #fff;
            color: #000000;
            border: 2px solid #000000;
            border-radius: 50px;
            font-weight: 700;
            transition: all 0.2s ease-in-out;
        }}
        .meal-btn:hover {{ background: #f5f5f5; }}
        .active-meal {{ background: #000000 !important; color: white !important; }}
        
        .food-card {{
            background: {chosen_card_bg};
            border-left: 8px solid {chosen_border};
            padding: 30px;
            border-radius: 16px;
            box-shadow: 0 6px 20px rgba(0,0,0,0.04);
            transition: all 0.4s ease-in-out;
        }}
        ul {{ list-style-type: none; padding: 0; margin: 0; }}
        li {{
            font-size: 1.25em;
            padding: 14px 0;
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            font-weight: 500;
        }}
        li:last-child {{ border-bottom: none; }}
        li::before {{
            content: "✨ ";
            margin-right: 12px;
        }}
    </style>
    """
    
    html += "<div class='container'>"
    html += "<h1>✨ Munnawer Khan's Family Week Meal Plan ✨</h1>"
    html += "<p class='subtitle'>Click a Day and select a Meal type below</p>"
    
    html += "<div class='tabs'>"
    for day in meal_plan.keys():
        css_class = "tab-btn active-day" if day == selected_day else "tab-btn"
        html += f"<a class='{css_class}' href='/?day={day}&meal={selected_meal}'>{day[:3]}</a>"
    html += "</div>"
    
    html += "<div class='meal-menu'>"
    meals_list = ["Breakfast", "Lunch", "Snacks", "Dinner"]
    emojis = {"Breakfast": "🍳", "Lunch": "🥪", "Snacks": "🍫", "Dinner": "🍲"}
    
    for m in meals_list:
        css_class = "meal-btn active-meal" if m == selected_meal else "meal-btn"
        html += f"<a class='{css_class}' href='/?day={selected_day}&meal={m}'>{emojis[m]} {m}</a>"
    html += "</div>"
    
    html += "<div class='food-card'>"
    html += f"<h2 style='color: #000000; margin-top:0;'>🍱 {selected_day} - {selected_meal} Options:</h2>"
    html += "<ul>"
    
    current_options = meal_plan[selected_day][selected_meal]
    for option in current_options:
        html += f"<li>{option}</li>"
        
    html += "</ul>"
    html += "</div>"
    html += "</div>"
    
    return html

if __name__ == '__main__':
    app.run(debug=True)
