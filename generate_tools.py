#!/usr/bin/env python3
"""
Generate tool entries for the AI tools directory.
Maps categories to appropriate emojis and formats HTML.
"""

tools = [
    (1, "Google Gemini", "assistant/search", "91.2", "4.7", "28.2m", "Freemium + subscriptions", "Google's multimodal AI assistant. Deep research capabilities and native app integration."),
    (2, "Sora by OpenAI", "video/avatars", "90.5", "4.8", "225k", "Freemium + in-app", "OpenAI's text-to-video model. Cinematic 4K video generation from text prompts."),
    (3, "Google NotebookLM", "assistant/search", "89.7", "4.9", "24k", "Freemium", "Google's AI research assistant. Turns documents into podcasts and summaries."),
    (4, "ChatGPT", "assistant/search", "89.2", "4.7", "44.4m", "Freemium + subscription", "OpenAI's conversational AI. The original viral chatbot with broad capabilities."),
    (5, "Microsoft Copilot AI Assistant", "assistant/search", "88.3", "4.7", "2.2m", "Freemium + Microsoft 365", "Microsoft's AI across Windows and Office. Deep integration with productivity suite."),
    (6, "Meta AI - Vibes & AI Glasses", "assistant/search", "87.3", "4.7", "65k", "Free", "Meta's AI assistant with multimodal features. Powers Ray-Ban smart glasses."),
    (7, "Perplexity", "assistant/search", "85.2", "4.8", "416k", "Freemium + subscription", "AI search engine with citations. Real-time web access with source transparency."),
    (8, "Claude", "assistant/search", "84.0", "4.7", "47k", "Freemium + subscription", "Anthropic's AI assistant. Known for long context and thoughtful responses."),
    (9, "Writesonic", "writing/seo", "79.1", "4.8", "2.1k", "Paid plans", "AI writing platform for marketing copy. SEO-optimized content generation."),
    (10, "Jasper", "writing/seo", "78.9", "4.8", "1.9k", "Paid plans", "Enterprise AI writing assistant. Long-form content and brand voice management."),
    (11, "Zoom Workplace", "business/ops", "77.9", "4.6", "14.5k", "Freemium + plans", "AI-powered meeting and collaboration platform. Video conferencing with smart features."),
    (12, "Adobe Creative Cloud", "image/design", "78.8", "4.7", "7.3k", "Subscription", "Suite of creative tools with AI features. Photoshop, Illustrator with generative AI."),
    (13, "Grammarly Business", "writing/seo", "78.8", "4.7", "7.2k", "Subscription", "AI writing assistant for teams. Grammar, tone, and clarity suggestions."),
    (14, "Surfer", "writing/seo", "78.6", "4.9", "421", "Subscription", "SEO content optimization platform. Data-driven writing recommendations."),
    (15, "RunwayML", "video/avatars", "78.4", "4.5", "7.8k", "Freemium + subscription", "AI video editing and generation suite. Professional video creation tools."),
    (16, "Blaze", "writing/seo", "77.7", "4.8", "699", "Subscription", "AI content creation for marketers. Brand voice and multi-channel publishing."),
    (17, "Anyword", "writing/seo", "76.9", "4.8", "391", "Subscription", "AI copywriting with predictive performance. Data-driven marketing copy."),
    (18, "Virbo", "video/avatars", "76.1", "4.9", "104", "Subscription", "AI avatar video creation. Multilingual talking head videos."),
    (19, "HoneyBook", "business/ops", "75.9", "4.7", "673", "Subscription", "Business management for creatives. CRM, contracts, and invoicing."),
    (20, "FeedHive", "business/ops", "75.6", "4.9", "85", "Subscription", "AI-powered social media management. Content recycling and scheduling."),
    (21, "neuroflash", "writing/seo", "75.6", "4.8", "184", "Subscription", "AI text and image generation. European alternative with GDPR compliance."),
    (22, "ProWritingAid", "writing/seo", "75.1", "4.7", "497", "Freemium + subscription", "Writing improvement platform. Style, grammar, and structure analysis."),
    (23, "Pictory", "video/avatars", "75.0", "4.8", "162", "Subscription", "AI video creation from text. Automatic summarization and editing."),
    (24, "1min.AI", "writing/seo", "74.6", "4.7", "433", "Freemium", "All-in-one AI platform. Writing, images, and more in one tool."),
    (25, "Fliki", "video/avatars", "74.5", "4.7", "345", "Freemium + subscription", "Text to video with AI voices. Blog-to-video conversion."),
    (26, "HeyGen", "video/avatars", "74.5", "4.7", "307", "Subscription", "AI avatar video creation. Professional spokesperson videos at scale."),
    (27, "Simplified", "writing/seo", "74.4", "4.7", "302", "Freemium + subscription", "All-in-one marketing platform. Design, video, writing, and publishing."),
    (28, "Synthesia", "video/avatars", "74.0", "4.6", "313", "Subscription", "AI video generation with avatars. Training and explainer videos."),
    (29, "TextCortex AI", "writing/seo", "73.9", "4.7", "236", "Freemium + subscription", "Personalized AI writing assistant. Learns your style over time."),
    (30, "Fusebase", "business/ops", "73.7", "4.7", "175", "Subscription", "AI-powered client portals. Collaborative workspaces with smart features."),
    (31, "contents.ai", "writing/seo", "73.2", "4.6", "154", "Subscription", "AI content generation platform. Multi-language SEO content."),
    (32, "Rezolve AI", "business/ops", "73.0", "4.8", "9", "Enterprise", "Conversational commerce platform. AI shopping assistants for retail."),
    (33, "Craftly.AI", "writing/seo", "72.9", "4.8", "9", "Subscription", "AI copywriting assistant. Marketing and creative content generation."),
    (34, "TrendSights", "business/ops", "72.9", "4.8", "19", "Subscription", "AI market intelligence. Trend forecasting and consumer insights."),
    (35, "Reelcraft.ai", "video/avatars", "72.8", "4.8", "20", "Freemium", "AI video creation from text. Social media short-form content."),
    (36, "Akool", "video/avatars", "72.6", "5.0", "21", "Subscription", "AI avatar and image generation. Personalized marketing content."),
    (37, "Lately", "business/ops", "72.6", "4.9", "7", "Subscription", "AI social media management. Repurposes long-form content automatically."),
    (38, "Fosfor Decision Cloud", "business/ops", "72.6", "4.9", "7", "Enterprise", "AI-powered business intelligence. Decision support and analytics."),
    (39, "Rytr", "writing/seo", "72.5", "4.6", "18", "Freemium + subscription", "AI writing assistant. Quick copy generation across formats."),
    (40, "ElevenLabs", "audio/voice", "72.4", "4.7", "17", "Freemium + subscription", "AI voice synthesis and cloning. Ultra-realistic text-to-speech."),
    (41, "Leonardo AI", "image/design", "72.4", "5.0", "10", "Freemium + subscription", "AI art and image generation. Game assets and creative visuals."),
    (42, "Easy-Peasy.AI", "writing/seo", "72.3", "4.9", "10", "Freemium", "AI content and image generation. Simple interface for beginners."),
    (43, "Texta.ai", "writing/seo", "72.2", "4.6", "345", "Subscription", "AI article writing. Bulk content generation for blogs."),
    (44, "InVideo", "video/avatars", "72.1", "4.6", "407", "Freemium + subscription", "AI video creation platform. Templates and automated editing."),
    (45, "Photoleap", "image/design", "72.1", "4.8", "6", "Freemium + subscription", "AI photo editing app. Creative image manipulation on mobile."),
    (46, "Facetune", "image/design", "72.1", "4.8", "6", "Freemium + subscription", "AI photo retouching. Portrait enhancement and editing."),
    (47, "CoSupport AI", "business/ops", "72.0", "5.0", "10", "Enterprise", "AI customer support platform. Automated ticket resolution."),
    (48, "CausalFunnel", "business/ops", "71.9", "5.0", "7", "Subscription", "AI conversion optimization. Predictive funnel analytics."),
    (49, "Straico", "business/ops", "71.9", "5.0", "7", "Subscription", "Multi-model AI platform. Access to various LLMs in one place."),
    (50, "AI Docs", "business/ops", "71.9", "5.0", "7", "Subscription", "AI document processing. Automated data extraction and analysis."),
    (51, "storywise", "business/ops", "71.9", "5.0", "6", "Subscription", "AI user research platform. Interview analysis and insights."),
    (52, "Quest", "business/ops", "71.9", "5.0", "6", "Subscription", "AI sales assistant. Automated outreach and follow-ups."),
    (53, "Brume", "business/ops", "71.9", "5.0", "6", "Subscription", "AI workflow automation. No-code process automation."),
    (54, "Tabnine", "dev/data", "71.8", "4.6", "5", "Freemium + subscription", "AI code completion. IDE plugin for developers."),
    (55, "Clarifai", "dev/data", "71.8", "4.6", "5", "Enterprise", "AI platform for computer vision. Image and video recognition."),
    (56, "Ervy", "business/ops", "71.8", "5.0", "5", "Subscription", "AI meeting assistant. Automated notes and action items."),
    (57, "Flagright", "business/ops", "71.8", "4.9", "12", "Enterprise", "AI fraud detection. Financial crime prevention platform."),
    (58, "Max AI", "dev/data", "71.7", "4.6", "15", "Freemium", "AI document analysis. Chat with PDFs and documents."),
    (59, "Ada", "business/ops", "71.7", "4.7", "15", "Enterprise", "AI customer service automation. Conversational AI for support."),
    (60, "Adobe Firefly", "image/design", "71.6", "4.4", "18", "Subscription", "Adobe's generative AI. Safe commercial image generation."),
    (61, "DALL-E 3", "image/design", "71.6", "4.4", "21", "Credits/subscription", "OpenAI's image generator. Detailed text-to-image creation."),
    (62, "Mini Course Generator", "business/ops", "71.5", "4.7", "21", "Subscription", "AI course creation. Automated educational content."),
    (63, "Synthesys Studio", "video/avatars", "71.4", "4.5", "21", "Subscription", "AI voice and video generation. Multi-language content."),
    (64, "Forethought", "business/ops", "71.3", "4.5", "10", "Enterprise", "AI customer support platform. Predictive ticket routing."),
    (65, "Inxide", "business/ops", "71.3", "4.6", "10", "Subscription", "AI business intelligence. Data analysis and reporting."),
    (66, "GrowthBar", "writing/seo", "71.2", "4.8", "8", "Subscription", "AI SEO and writing tool. Keyword research and content optimization."),
    (67, "mesha", "business/ops", "71.2", "5.0", "8", "Subscription", "AI accounting automation. Smart bookkeeping and invoicing."),
    (68, "Hal9", "business/ops", "71.2", "4.5", "8", "Subscription", "AI data analytics. Natural language queries on databases."),
    (69, "WRITER", "business/ops", "71.1", "4.5", "8", "Enterprise", "AI writing platform for enterprises. Brand-consistent content."),
    (70, "Adobe Target", "business/ops", "71.0", "4.0", "6", "Enterprise", "AI-powered A/B testing. Personalization and optimization."),
    (71, "Article Forge", "writing/seo", "70.9", "4.0", "7", "Subscription", "AI article writer. Long-form content automation."),
    (72, "Copysmith", "writing/seo", "70.8", "4.2", "27", "Subscription", "AI copywriting for e-commerce. Product descriptions at scale."),
    (73, "Sloyd", "image/design", "70.7", "4.2", "47", "Freemium", "AI 3D model generation. Game-ready asset creation."),
    (74, "Skai", "business/ops", "70.7", "4.3", "42", "Enterprise", "AI marketing platform. Cross-channel campaign optimization."),
    (75, "SingleStore", "dev/data", "70.7", "4.5", "39", "Subscription", "Real-time AI database. Fast analytics and transactions."),
    (76, "MailMaestro", "writing/seo", "70.6", "4.3", "51", "Freemium", "AI email assistant. Professional email drafting."),
    (77, "LongShot AI", "writing/seo", "70.6", "4.5", "51", "Subscription", "AI long-form writing. Fact-checked content generation."),
    (78, "Sunoh", "business/ops", "70.5", "4.1", "35", "Subscription", "AI clinical documentation. Medical note automation."),
    (79, "Breeze", "business/ops", "70.5", "4.5", "34", "Subscription", "HubSpot's AI features. Marketing and sales automation."),
    (80, "Beautiful.ai", "business/ops", "70.4", "4.3", "84", "Subscription", "AI presentation maker. Smart slide design."),
    (81, "NightCafe", "image/design", "70.4", "4.7", "83", "Credits", "AI art community and generator. Multiple style models."),
    (82, "Replit", "dev/data", "70.4", "4.4", "154", "Freemium + subscription", "AI-powered coding platform. Cloud IDE with Ghostwriter."),
    (83, "FlexClip", "video/avatars", "70.3", "4.5", "127", "Freemium + subscription", "AI video maker. Templates and easy editing."),
    (84, "CoPilot AI", "business/ops", "70.3", "4.6", "118", "Subscription", "AI sales automation. LinkedIn prospecting assistant."),
    (85, "B12", "business/ops", "70.2", "4.1", "113", "Subscription", "AI website builder. Professional sites with smart features."),
    (86, "eloomi", "business/ops", "70.2", "4.4", "95", "Subscription", "AI learning platform. Personalized training paths."),
    (87, "Copy.ai", "writing/seo", "70.1", "4.4", "67", "Freemium + subscription", "AI marketing copywriter. Social media and ad copy."),
    (88, "LOVO", "audio/voice", "70.0", "4.5", "57", "Subscription", "AI voice generator. Emotional text-to-speech."),
    (89, "memoQ TMS", "dev/data", "69.9", "4.6", "55", "Subscription", "AI translation management. Professional localization platform."),
    (90, "Opus Clip", "video/avatars", "69.8", "3.6", "5", "Subscription", "AI video repurposing. Long-form to short-form content."),
    (91, "D-ID", "video/avatars", "69.6", "2.7", "7", "Credits", "AI avatar creation. Talking photos and videos."),
    (92, "CredoHire", "business/ops", "69.6", "4.2", "5", "Subscription", "AI recruitment platform. Automated candidate screening."),
    (93, "Photoleap", "image/design", "69.6", "4.8", "6", "Freemium + subscription", "AI photo editing app. Creative image manipulation."),
    (94, "Facetune", "image/design", "69.6", "4.8", "6", "Freemium + subscription", "AI portrait enhancement. Selfie editing and retouching."),
    (95, "CoSupport AI", "business/ops", "69.6", "5.0", "10", "Enterprise", "AI customer support platform. Ticket automation."),
    (96, "Blocks", "business/ops", "69.3", "5.0", "1", "Subscription", "AI contract automation. Smart document generation."),
    (97, "AdCreative.ai", "business/ops", "67.4", "3.4", "165", "Subscription", "AI ad creative generation. Multi-platform ad designs."),
    (98, "vcita", "business/ops", "67.0", "4.4", "289", "Subscription", "AI business management. CRM and scheduling for SMBs."),
    (99, "TextCortex AI", "writing/seo", "66.9", "4.7", "236", "Freemium + subscription", "AI writing companion. Personalized content assistant."),
    (100, "DeepSeek - AI Assistant", "assistant/search", "65.0", "3.8", "250k", "Freemium", "Chinese AI assistant. Open-source competitive model."),
]

# Category to emoji mapping
emoji_map = {
    "assistant/search": "🔍",
    "video/avatars": "🎬",
    "writing/seo": "✍️",
    "business/ops": "💼",
    "image/design": "🎨",
    "audio/voice": "🎙️",
    "dev/data": "💻",
}

# Category to filter mapping
category_map = {
    "assistant/search": "productivity",
    "video/avatars": "design",
    "writing/seo": "writing",
    "business/ops": "productivity",
    "image/design": "design",
    "audio/voice": "audio",
    "dev/data": "coding",
}

def stars_from_rating(rating):
    """Convert rating to star display"""
    r = float(rating)
    if r >= 4.8:
        return "★★★★★"
    elif r >= 4.5:
        return "★★★★★"
    elif r >= 4.0:
        return "★★★★☆"
    elif r >= 3.5:
        return "★★★★☆"
    elif r >= 3.0:
        return "★★★☆☆"
    else:
        return "★★☆☆☆"

def format_count(count):
    """Format review count"""
    if "m" in count.lower():
        return count.upper()
    elif "k" in count.lower():
        return count.upper()
    else:
        return count

def generate_tool_html(rank, name, category, rating, count, price, description):
    emoji = emoji_map.get(category, "🤖")
    data_category = category_map.get(category, "productivity")
    stars = stars_from_rating(rating)
    formatted_count = format_count(count)
    
    # Format price display
    if "free" in price.lower():
        price_html = '<span class="price">FREE</span>'
    elif "$" in price:
        # Extract price if possible
        price_html = f'<span class="price">{price}</span>'
    else:
        price_html = f'<span class="price">{price}</span>'
    
    # Create URL-friendly anchor
    anchor = name.lower().replace(" ", "-").replace(".", "").replace("(", "").replace(")", "").replace("&", "and")[:30]
    
    html = f'''            <article class="tool-row" data-category="{data_category}">
                <div class="tool-rank">#{rank}</div>
                <div class="tool-main">
                    <div class="tool-identity">
                        <span class="tool-emoji">{emoji}</span>
                        <div>
                            <h3>{name}</h3>
                            <p class="tool-tagline">{description}</p>
                        </div>
                    </div>
                    <div class="tool-tags">
                        <span class="tag">{category.split("/")[0].title()}</span>
                    </div>
                    <div class="tool-rating">
                        <span class="stars">{stars}</span>
                        <span class="count">{formatted_count}</span>
                    </div>
                    <div class="tool-price">
                        {price_html}
                    </div>
                </div>
                <a href="https://www.google.com/search?q={name.replace(" ", "+")}+AI+tool" target="_blank" rel="noopener" class="tool-action" data-tool="{anchor}">
                    Try Free →
                </a>
            </article>'''
    return html

# Generate all tool entries
print("Generating tool entries...")
for tool in tools:
    rank, name, category, composite, rating, count, price, description = tool
    print(generate_tool_html(rank, name, category, rating, count, price, description))
    print()
