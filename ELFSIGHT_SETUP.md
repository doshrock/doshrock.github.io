# Elfsight Google Reviews Widget Setup Guide

Follow these steps to get your Google Reviews displaying automatically on your website.

---

## Step 1: Sign Up for Elfsight

1. Go to: **https://elfsight.com/google-reviews-widget/**
2. Click **"Try it for free"** or **"Start Free Trial"**
3. Sign up with your email (or use Google/Facebook login)
4. **Free Plan**: Allows up to 200 widget views per month

---

## Step 2: Create Your Widget

### 2.1 Connect Your Google Business
1. After signing in, click **"Create Widget"**
2. Choose **"Google Reviews"**
3. Enter your business name: **"Doshrock"**
4. Or paste your Google Maps URL: `https://maps.app.goo.gl/T9RvBhv4FG2nTNir6`
5. Click **"Connect"**

### 2.2 Customize the Widget Design

**Recommended Settings:**

**Layout Tab:**
- Layout: **Grid** or **Slider** (Grid looks better with 3 reviews)
- Reviews per page: **3**
- Columns: **3** (for desktop)

**Content Tab:**
- Show only: **5-star reviews** (optional)
- Show photos: **Yes**
- Show reviewer names: **Yes**
- Show dates: **Yes**

**Style Tab:**
- Theme: **Light** (matches your white cards)
- Primary color: **#F05F40** (your orange theme)
- Font: Choose one that matches your site (Arial or similar)
- Border radius: **10px** (matches your design)

**Header Tab:**
- Show header: **Yes**
- Title: "What Our Customers Say"
- Show rating: **Yes**
- Show review count: **Yes**

---

## Step 3: Get Your Widget Code

1. After customizing, click **"Save"** or **"Publish"**
2. You'll see an **"Installation"** or **"Get Code"** button
3. Click it and you'll see code like this:

```html
<script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
<div class="elfsight-app-abc123def456"></div>
```

4. **Copy this entire code** (both lines)

---

## Step 4: Add Code to Your Website

1. Open the file: `_includes/reviews.html`
2. Find this section (around line 15-27):

```html
<!--
============================================================
PASTE YOUR ELFSIGHT WIDGET CODE HERE
============================================================
...
-->
```

3. **Replace the entire comment block** with your Elfsight code
4. **Delete the temporary placeholder** (lines 29-40) - the section with "Setting up your Google Reviews..."

### Example - Before:
```html
<!--
============================================================
PASTE YOUR ELFSIGHT WIDGET CODE HERE
============================================================
...
-->

<!-- Temporary placeholder - Remove this after adding Elfsight code above -->
<div style="background: white; padding: 40px...">
    ...
</div>
<!-- End temporary placeholder -->
```

### Example - After:
```html
<script src="https://static.elfsight.com/platform/platform.js" data-use-service-core defer></script>
<div class="elfsight-app-abc123def456"></div>
```

---

## Step 5: Save and Deploy

1. **Save** the file `_includes/reviews.html`
2. **Commit** and **push** to GitHub:
   ```bash
   git add _includes/reviews.html
   git commit -m "Add Elfsight Google Reviews widget"
   git push
   ```
3. Wait 1-2 minutes for GitHub Pages to rebuild
4. Visit your website and scroll to the Reviews section!

---

## Troubleshooting

### Widget Not Showing?
1. **Check the code**: Make sure both lines (script + div) are pasted
2. **Check your plan**: Free plan has 200 views/month limit
3. **Clear browser cache**: Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
4. **Check browser console**: Right-click → Inspect → Console tab for errors

### Want to Change Design?
1. Go back to Elfsight dashboard
2. Find your widget and click "Edit"
3. Make changes and click "Save"
4. Changes appear on your site automatically (no code update needed!)

---

## Free Plan Limitations

- **200 widget views per month** (should be fine for small traffic)
- **Elfsight branding** displayed on widget
- **Basic support**

If you need more, consider:
- **Pro plan**: $5-10/month for more views and no branding
- **Or**: Go back to the manual approach (zero cost, full control)

---

## Alternative: Manual Approach

If you decide Elfsight isn't worth it, let me know and I can restore the beautiful manual review system we built earlier (with random rotation).

---

**Questions?** Open an issue on GitHub or contact Claude for help!
