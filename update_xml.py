import xml.etree.ElementTree as ET
import os

# Path to the XML file
xml_file_path = 'assets/data/menu.xml'

# Detailed descriptions for specific items
# Format: Key (partial match) -> (French, English, Korean)
item_descriptions = {
    # Appetizers
    "Shrimp Fries": (
        "Frites croustillantes garnies de crevettes succulentes et d'une sauce spéciale.",
        "Crispy fries topped with succulent shrimp and a special sauce.",
        "바삭한 감자튀김 위에 통통한 새우와 특제 소스를 얹은 별미입니다."
    ),
    "Gim-mari": (
        "Rouleaux d'algues frits farcis de nouilles de verre, un classique de la cuisine de rue.",
        "Deep-fried seaweed rolls stuffed with glass noodles, a street food classic.",
        "당면을 김으로 말아 바삭하게 튀겨낸 한국 분식의 대표 주자입니다."
    ),
    "Mandu": (
        "Dumplings coréens frits, croustillants à l'extérieur et juteux à l'intérieur.",
        "Fried Korean dumplings, crispy on the outside and juicy on the inside.",
        "겉은 바삭하고 속은 촉촉한 한국식 군만두입니다."
    ),
    "Chicken Sw& Sp": (
        "Poulet frit croustillant enrobé d'une sauce aigre-douce et épicée.",
        "Crispy fried chicken coated in a sweet and spicy sauce.",
        "매콤달콤한 양념이 어우러진 바삭한 닭강정입니다."
    ),
    "Chicken - Soy": (
        "Poulet frit croustillant glacé d'une sauce soja à l'ail savoureuse.",
        "Crispy fried chicken glazed with a savory soy garlic sauce.",
        "짭조름한 간장 마늘 소스가 일품인 닭강정입니다."
    ),
    "Snow Oninon": (
        "Poulet frit surmonté d'oignons frais et d'une sauce blanche crémeuse.",
        "Fried chicken topped with fresh onions and a creamy white sauce.",
        "아삭한 양파와 부드러운 크림 소스가 어우러진 치킨입니다."
    ),
    "Cheese Buldak": (
        "Poulet très épicé recouvert de fromage fondu pour adoucir le feu.",
        "Very spicy chicken covered in melted cheese to balance the heat.",
        "화끈하게 매운 불닭에 고소한 치즈를 듬뿍 얹었습니다."
    ),
    "French Fries": (
        "Frites classiques, dorées et croustillantes.",
        "Classic fries, golden and crispy.",
        "바삭하고 고소한 클래식 감자튀김입니다."
    ),
    "Vege Fritters": (
        "Beignets de légumes variés, croustillants et légers.",
        "Assorted vegetable fritters, crispy and light.",
        "다양한 야채를 튀겨낸 바삭하고 고소한 야채튀김입니다."
    ),
    "Rice": (
        "Bol de riz blanc cuit à la vapeur.",
        "Bowl of steamed white rice.",
        "갓 지어낸 따뜻한 공기밥입니다."
    ),
    "Kimchi": (
        "Chou fermenté épicé, l'accompagnement essentiel de la cuisine coréenne.",
        "Spicy fermented cabbage, the essential side dish of Korean cuisine.",
        "한국인의 밥상에 빠질 수 없는 매콤하고 아삭한 김치입니다."
    ),
    "Kimchi-jeon": (
        "Crêpe coréenne croustillante au kimchi et aux légumes.",
        "Crispy Korean pancake made with kimchi and vegetables.",
        "잘 익은 김치로 부쳐낸 매콤하고 바삭한 김치전입니다."
    ),
    "Seaweed Salad": (
        "Salade d'algues assaisonnée, fraîche et légère.",
        "Seasoned seaweed salad, fresh and light.",
        "새콤달콤하게 양념된 신선한 미역 샐러드입니다."
    ),
    "Miso": (
        "Soupe miso traditionnelle, chaude et réconfortante.",
        "Traditional miso soup, warm and comforting.",
        "따뜻하고 구수한 미소 된장국입니다."
    ),
    
    # Bunsik
    "Japchae": (
        "Nouilles de patate douce sautées avec des légumes et de la viande, un plat de fête.",
        "Stir-fried sweet potato noodles with vegetables and meat, a festive dish.",
        "쫄깃한 당면과 야채, 고기를 볶아낸 한국의 잔치 음식입니다."
    ),
    "Mandu-guk": (
        "Soupe de dumplings dans un bouillon riche et savoureux.",
        "Dumpling soup in a rich and savory broth.",
        "진한 육수에 속이 꽉 찬 만두를 넣고 끓인 만두국입니다."
    ),
    "Ramen": (
        "Nouilles instantanées coréennes servies dans un bouillon chaud.",
        "Korean instant noodles served in a hot broth.",
        "얼큰한 국물과 쫄깃한 면발이 일품인 한국 라면입니다."
    ),
    "Tteokbokki": (
        "Gâteaux de riz mijotés dans une sauce pimentée douce et épicée.",
        "Rice cakes simmered in a sweet and spicy chili sauce.",
        "매콤달콤한 고추장 소스에 쫄깃한 떡이 어우러진 국민 간식입니다."
    ),
    
    # Doshrock
    "Bulgogi Doshrock": (
        "Boîte-repas avec bœuf mariné grillé, riz et accompagnements.",
        "Lunch box with grilled marinated beef, rice, and sides.",
        "달콤 짭짤한 불고기와 반찬이 담긴 든든한 도시락입니다."
    ),
    "Jeyuk Doshrock": (
        "Boîte-repas avec porc épicé sauté, riz et accompagnements.",
        "Lunch box with spicy stir-fried pork, rice, and sides.",
        "매콤한 제육볶음과 반찬이 어우러진 맛있는 도시락입니다."
    ),
    "Samgyupsal Doshrock": (
        "Boîte-repas avec poitrine de porc grillée, riz et accompagnements.",
        "Lunch box with grilled pork belly, rice, and sides.",
        "노릇하게 구운 삼겹살과 반찬을 즐길 수 있는 도시락입니다."
    ),
    "Donkatsu Doshrock": (
        "Boîte-repas avec côtelette de porc panée, riz et accompagnements.",
        "Lunch box with breaded pork cutlet, rice, and sides.",
        "바삭한 돈까스와 반찬이 포함된 푸짐한 도시락입니다."
    ),
    "Chicken-katsu Doshrock": (
        "Boîte-repas avec filet de poulet pané, riz et accompagnements.",
        "Lunch box with breaded chicken cutlet, rice, and sides.",
        "부드러운 치킨까스와 반찬이 어우러진 도시락입니다."
    ),
    "Kkanpoong Doshrock": (
        "Boîte-repas avec poulet frit à l'ail et au piment, riz et accompagnements.",
        "Lunch box with spicy garlic fried chicken, rice, and sides.",
        "매콤한 깐풍기와 반찬을 함께 즐기는 별미 도시락입니다."
    ),
    "Chicken-galbi Doshrock": (
        "Boîte-repas avec poulet épicé sauté, riz et accompagnements.",
        "Lunch box with spicy stir-fried chicken, rice, and sides.",
        "매콤한 닭갈비와 반찬이 담긴 맛있는 도시락입니다."
    ),
    "BBQ-Combo": (
        "Assortiment de viandes grillées (Bœuf, Porc, Poulet) avec riz.",
        "Assortment of grilled meats (Beef, Pork, Chicken) with rice.",
        "불고기, 제육, 닭갈비를 한 번에 즐길 수 있는 모둠 도시락입니다."
    ),
    
    # Dupbap
    "Bulgogi Dupbap": (
        "Bol de riz surmonté de bœuf mariné et de légumes.",
        "Rice bowl topped with marinated beef and vegetables.",
        "밥 위에 달콤 짭짤한 불고기를 듬뿍 얹은 덮밥입니다."
    ),
    "Jeyuk Dupbap": (
        "Bol de riz surmonté de porc épicé et de légumes.",
        "Rice bowl topped with spicy pork and vegetables.",
        "밥 위에 매콤한 제육볶음을 듬뿍 얹은 덮밥입니다."
    ),
    "Tuna Mayo": (
        "Bol de riz avec thon, mayonnaise et algues.",
        "Rice bowl with tuna, mayonnaise, and seaweed.",
        "고소한 참치 마요네즈와 김가루가 어우러진 덮밥입니다."
    ),
    "Chicken Mayo": (
        "Bol de riz avec poulet frit, mayonnaise et sauce soja.",
        "Rice bowl with fried chicken, mayonnaise, and soy sauce.",
        "바삭한 치킨과 고소한 마요네즈가 조화를 이루는 덮밥입니다."
    ),
    "Kimchi Bokkeumbap": (
        "Riz sauté au kimchi épicé, souvent servi avec un œuf.",
        "Spicy kimchi fried rice, often served with an egg.",
        "잘 익은 김치로 매콤하게 볶아낸 김치볶음밥입니다."
    ),
    
    # Gimbap
    "Classic Gimbap": (
        "Rouleau de riz aux légumes variés, jambon et œuf.",
        "Rice roll with assorted vegetables, ham, and egg.",
        "다양한 야채와 햄, 계란이 들어간 기본 김밥입니다."
    ),
    "Bulgogi Gimbap": (
        "Rouleau de riz garni de bœuf mariné savoureux.",
        "Rice roll filled with savory marinated beef.",
        "달콤 짭짤한 불고기가 듬뿍 들어간 김밥입니다."
    ),
    "Tuna Gimbap": (
        "Rouleau de riz garni de thon et de mayonnaise.",
        "Rice roll filled with tuna and mayonnaise.",
        "고소한 참치와 마요네즈가 어우러진 인기 김밥입니다."
    ),
    "Donkatsu Gimbap": (
        "Rouleau de riz garni d'une côtelette de porc croustillante.",
        "Rice roll filled with a crispy pork cutlet.",
        "바삭한 돈까스가 통째로 들어간 든든한 김밥입니다."
    ),
    "Kimcheese Gimbap": (
        "Rouleau de riz avec kimchi sauté et fromage fondant.",
        "Rice roll with stir-fried kimchi and melting cheese.",
        "매콤한 김치와 고소한 치즈가 만난 별미 김밥입니다."
    ),
    
    # Bibimbap
    "Vege Bibimbap": (
        "Riz mélangé avec un assortiment de légumes frais et un œuf.",
        "Mixed rice with an assortment of fresh vegetables and an egg.",
        "신선한 나물과 야채를 고추장에 비벼 먹는 건강식입니다."
    ),
    "Tofu Bibimbap": (
        "Bibimbap végétarien garni de tofu poêlé.",
        "Vegetarian bibimbap topped with pan-fried tofu.",
        "담백한 두부를 얹어 더욱 건강한 비빔밥입니다."
    ),
    "Bulgogi Bibimbap": (
        "Bibimbap garni de bœuf mariné tendre.",
        "Bibimbap topped with tender marinated beef.",
        "불고기를 더해 더욱 풍성하고 맛있는 비빔밥입니다."
    ),
    "Chicken Bibimbap": (
        "Bibimbap garni de poulet mariné.",
        "Bibimbap topped with marinated chicken.",
        "담백한 치킨을 얹어 맛을 낸 비빔밥입니다."
    ),
    "Dolsot": (
        "Bibimbap servi dans un bol en pierre chaud, rendant le riz croustillant.",
        "Bibimbap served in a hot stone bowl, making the rice crispy.",
        "뜨거운 돌솥에 담아 마지막까지 따뜻하고 바삭하게 즐기는 비빔밥입니다."
    ),
    
    # Jjigae
    "Kimchi Jjigae": (
        "Ragoût épicé au kimchi, porc et tofu.",
        "Spicy stew with kimchi, pork, and tofu.",
        "잘 익은 김치와 돼지고기를 넣고 얼큰하게 끓인 찌개입니다."
    ),
    "Doenjang Jjigae": (
        "Ragoût de pâte de soja fermentée avec légumes et tofu.",
        "Soybean paste stew with vegetables and tofu.",
        "구수한 된장 국물에 야채와 두부를 넣은 찌개입니다."
    ),
    "Chadol Doenjang": (
        "Ragoût de pâte de soja avec poitrine de bœuf.",
        "Soybean paste stew with beef brisket.",
        "차돌박이를 넣어 더욱 고소하고 진한 된장찌개입니다."
    ),
    "Sundubu": (
        "Ragoût épicé de tofu soyeux, souvent avec des fruits de mer ou de la viande.",
        "Spicy soft tofu stew, often with seafood or meat.",
        "부드러운 순두부와 얼큰한 국물이 일품인 찌개입니다."
    ),
    "Sundaeguk": (
        "Soupe riche avec boudin coréen et viande de porc.",
        "Rich soup with Korean blood sausage and pork meat.",
        "진한 사골 육수에 순대와 고기가 들어간 든든한 국밥입니다."
    ),
    
    # Anju
    "Eomuk-tang": (
        "Soupe chaude de gâteaux de poisson, populaire en hiver.",
        "Hot fish cake soup, popular in winter.",
        "시원한 국물과 쫄깃한 어묵을 즐길 수 있는 탕 요리입니다."
    )
}

# Fallback templates
category_templates = {
    "Default": (
        "Un plat délicieux préparé avec des ingrédients frais.",
        "A delicious dish prepared with fresh ingredients.",
        "신선한 재료로 정성껏 만든 맛있는 요리입니다."
    )
}

def get_description(name, friendly_name):
    # Try to find a matching key in item_descriptions
    # Check friendly name first, then name
    search_str = friendly_name if friendly_name else name
    
    for key, desc_tuple in item_descriptions.items():
        if key.lower() in search_str.lower():
            return desc_tuple
            
    return category_templates["Default"]

def update_xml():
    if not os.path.exists(xml_file_path):
        print(f"Error: File not found at {xml_file_path}")
        return

    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        
        for category in root.findall(".//Category"):
            for item in category.findall("Item"):
                item_name = item.get('Name', '')
                friendly_name = item.get('MobileAppFriendlyName', item_name)
                
                # Get specific description
                desc_fr, desc_en, desc_kr = get_description(item_name, friendly_name)
                
                full_desc = f"{desc_fr} / {desc_en} / {desc_kr}"
                
                item.set('MobileAppDescription', full_desc)
                
        tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
        print("Successfully updated menu.xml with detailed multilingual descriptions.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    update_xml()
