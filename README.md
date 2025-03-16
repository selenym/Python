Here's the Bunny GIF that I created with 2 images using imageio lib!
![bunny](https://github.com/user-attachments/assets/0185046f-6c6f-4b31-b7d5-c55a3cd9c671)

[Up<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fortune Cookie</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 250px;
        }
        #quote {
            font-size: 100px;
            margin-top: px;
            font-style: italic;
        }
        button {
            background-color: #f4a261;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            margin-top: 20px;
            border-radius: 5px;
        }
        button:hover {
            background-color: #e76f51;
        }
    </style>
</head>
<body>

    <h1>🍪 Fortune Cookie 🍪</h1>
    <p id="quote">Click the button to reveal your fortune!</p>
    <button onclick="showFortune()">Get Fortune</button>

    <script>
        const quotes = [
            "Wherever you go, go with all your heart.",
            "You have a charming way with words and should write a book.",
            "From small beginnings come great things.",
            "An amazing adventure awaits you.",
            "Always have old memories and young hopes.",
            "When the flowers bloom, so will great joy in your heart.",
            "To shine is better than to reflect.",
            "Confucius says: He who has hope, has everything.",
            "You must know your own heart before you can know the heart of another.",
            "You are protected by silent love and friendship near you.",
            "The world will soon be ready to receive your talents.",
            "Now is the time to try something new. You will benefit.",
            "Your hard work is about to pay off.",
            "Good fortune takes preparation.",
            "The star of riches is shining on you.",
            "You will soon bring joy to someone.",
            "You will spend many years in comfort and material wealth.",
            "Next summer you will dance to a different beat.",
            "If you can befriend yourself, you will never be lonely.",
            "You will attract cultured and artistic people to your home.",
            "Your investments of time now will lead to success later."
        ];

        function showFortune() {
            const randomIndex = Math.floor(Math.random() * quotes.length);
            document.getElementById("quote").textContent = quotes[randomIndex];
        }
    </script>

</body>
</html>
loading Fortune_Cookies_HTML.html…]()
