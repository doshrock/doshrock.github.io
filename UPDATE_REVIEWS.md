# How to Update Google Reviews

This guide explains how to update the Google Reviews section on your website.

## How It Works

- The website stores **ALL** your 5-star Google reviews in `_data/reviews.yml`
- On each page visit, **3 random reviews** are selected and displayed
- This keeps the content fresh and shows different reviews to different visitors!

## Quick Update

To update reviews, simply edit the file: `_data/reviews.yml`

### Update Overall Rating

```yaml
overall_rating: 4.9  # Change this number
total_reviews: 242   # Change this number
```

### Add All Your Reviews

Each review has these fields:

```yaml
- name: "Reviewer Name"
  rating: 5          # Always 5 for featured reviews
  date: "2 weeks ago"
  text: "The review text goes here"
  avatar: "URL to profile picture"
  has_photo: true    # Set to false if no photo
  photo: "URL to review photo"
```

## How to Get Real Reviews from Google

### Step 1: Get Reviews from Google Maps

1. Go to your Google Business Profile
2. Click on "Reviews"
3. Find 5-star reviews with photos (if available)
4. Copy the reviewer's name, date, and review text

### Step 2: Get Review Photos

To get the photo URL from a Google review:
1. Open the review in Google Maps
2. Right-click on the photo
3. Select "Copy image address"
4. Paste the URL in the `photo` field

### Step 3: Get Reviewer Avatar

To get the reviewer's profile picture:
1. Click on their name in the review
2. Right-click on their profile picture
3. Select "Copy image address"
4. Paste the URL in the `avatar` field

**Note:** If you can't get the avatar URL, use this default:
```
https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y
```

## Example: Real Review Entry

```yaml
- name: "John Smith"
  rating: 5
  date: "1 week ago"
  text: "Amazing Korean food! The kimchi jjigae was perfect. Will definitely come back!"
  avatar: "https://lh3.googleusercontent.com/a-/AOh14Gj..."
  has_photo: true
  photo: "https://lh5.googleusercontent.com/p/AF1QipN..."
```

## Tips

- **Add as many reviews as you want!** The more reviews you add, the more variety visitors see
- Always use 5-star reviews only
- Include reviews with photos when possible (looks better!)
- Mix reviews in different languages if you have them (English, French, Korean)
- Update the overall rating monthly to keep it current
- Add new reviews as you get them to keep content fresh

## After Making Changes

1. Save the `_data/reviews.yml` file
2. Commit and push to GitHub
3. The website will automatically update

That's it! No need to touch any HTML, CSS, or JavaScript files.
