default_desc =  """Nowadays the lingerie industry is one of the most successful business spheres.
                We always stay in touch with the latest fashion tendencies - that is why our goods are so popular.."""

products = [
        {
            "name": "bootstrap-ring",
            "path": "product-details/bootstrap_ring",
            "img": "assets/img/bootstrap-ring.png",
            "price": "140",
            "desc": default_desc,
            "type": "new"},
        {
            "name": "purple_necklace",
            "path": "product-details/purple_necklace",
            "img": "assets/img/i.jpg",
            "price": "140",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "golden ring",
            "path": "product-details/golden_ring",
            "img": "assets/img/g.jpg",
            "price": "140",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "colorful_necklace",
            "path": "product-details/colorful_necklace",
            "img": "assets/img/s.png",
            "price": "160",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "purple_heart_necklace",
            "path": "product-details/purple_necklace",
            "img": "assets/img/i.jpg",
            "price": "140",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "queen_necklace",
            "path": "product-details/queen_necklace",
            "img": "assets/img/f.jpg",
            "price": "160",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "golden_ring_2",
            "path": "product-details/golden_ring",
            "img": "assets/img/h.jpg",
            "price": "160",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "blue_silver_ring",
            "path": "product-details/blue_silver_ring",
            "img": "assets/img/j.jpg",
            "price": "180",
            "desc": default_desc,
            "type": "new"},

        {
            "name": "queen_golden_bracelet",
            "path": "product-details/queen_golden_bracelet",
            "img": "assets/img/b.jpg",
            "price": "220",
            "desc": default_desc,
            "type": "normal"},

        {
            "name": "rings",
            "path": "product-details/rings",
            "img": "assets/img/c.jpg",
            "price": "220",
            "desc": default_desc,
            "type": "normal"},

        {
            "name": "golden_watch",
            "path": "product-details/golden_watch",
            "img": "assets/img/a.jpg",
            "price": "240",
            "desc": default_desc,
            "type": "normal"},

        {
            "name": "silver_rings",
            "path": "product-details/silver_rings",
            "img": "assets/img/d.jpg",
            "price": "270",
            "desc": default_desc,
            "type": "featured"},

        {
            "name": "golden_ring",
            "path": "product-details/golden_rings",
            "img":  "assets/img/e.jpg",
            "price": "200",
            "desc": default_desc,
            "type": "featured"},

        {
            "name": "queen_necklace",
            "path": "product-details/queen_necklace",
            "img": "assets/img/f.jpg",
            "price": "230",
            "desc": default_desc,
            "type": "featured"},

]

if __name__=="__main__":
    print([i for i in products if i["type"]=="featured"])