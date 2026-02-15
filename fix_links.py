#!/usr/bin/env python3
"""Replace Google search placeholder links with real tool URLs"""

import re

# Mapping of tool names to their real URLs
url_mapping = {
    'Google Gemini': 'https://gemini.google.com',
    'Sora by OpenAI': 'https://openai.com/sora',
    'Google NotebookLM': 'https://notebooklm.google.com',
    'ChatGPT': 'https://chatgpt.com',
    'Microsoft Copilot AI Assistant': 'https://copilot.microsoft.com',
    'Meta AI - Vibes & AI Glasses': 'https://www.meta.ai',
    'Perplexity': 'https://www.perplexity.ai',
    'Claude': 'https://claude.ai',
    'Writesonic': 'https://writesonic.com',
    'Jasper': 'https://www.jasper.ai',
    'Zoom Workplace': 'https://www.zoom.com',
    'Adobe Creative Cloud': 'https://www.adobe.com/creativecloud.html',
    'Grammarly Business': 'https://www.grammarly.com/business',
    'Surfer': 'https://surferseo.com',
    'RunwayML': 'https://runwayml.com',
    'Blaze': 'https://www.blaze.ai',
    'Anyword': 'https://anyword.com',
    'Virbo': 'https://virbo.wondershare.com',
    'HoneyBook': 'https://www.honeybook.com',
    'FeedHive': 'https://www.feedhive.com',
    'neuroflash': 'https://neuroflash.com',
    'ProWritingAid': 'https://prowritingaid.com',
    'Pictory': 'https://pictory.ai',
    '1min.AI': 'https://1min.ai',
    'Fliki': 'https://fliki.ai',
    'HeyGen': 'https://www.heygen.com',
    'Simplified': 'https://simplified.com',
    'Synthesia': 'https://www.synthesia.io',
    'TextCortex AI': 'https://textcortex.com',
    'Fusebase': 'https://fusebase.com',
    'contents.ai': 'https://contents.com',
    'Rezolve AI': 'https://rezolve.ai',
    'Craftly.AI': 'https://www.craftly.ai',
    'TrendSights': 'https://www.trendsights.ai',
    'Reelcraft.ai': 'https://www.reelcraft.ai',
    'Akool': 'https://akool.com',
    'Lately': 'https://www.lately.ai',
    'Fosfor Decision Cloud': 'https://fosfor.com',
    'Rytr': 'https://rytr.me',
    'ElevenLabs': 'https://elevenlabs.io',
    'Leonardo AI': 'https://leonardo.ai',
    'Easy-Peasy.AI': 'https://easy-peasy.ai',
    'Texta.ai': 'https://texta.ai',
    'InVideo': 'https://invideo.io',
    'Photoleap': 'https://www.photoleapapp.com',
    'Facetune': 'https://www.facetuneapp.com',
    'CoSupport AI': 'https://cosupport.ai',
    'CausalFunnel': 'https://causalfunnel.com',
    'Straico': 'https://straico.com',
    'AI Docs': 'https://www.aidocs.com',
    'storywise': 'https://www.storywise.ai',
    'Quest': 'https://www.quest.ai',
    'Brume': 'https://brume.xyz',
    'Tabnine': 'https://www.tabnine.com',
    'Clarifai': 'https://www.clarifai.com',
    'Ervy': 'https://www.ervy.ai',
    'Flagright': 'https://flagright.com',
    'Max AI': 'https://www.maxai.co',
    'Ada': 'https://www.ada.cx',
    'Adobe Firefly': 'https://www.adobe.com/products/firefly.html',
    'DALL-E 3': 'https://openai.com/dall-e-3',
    'Mini Course Generator': 'https://minicoursegenerator.com',
    'Synthesys Studio': 'https://synthesys.io',
    'Forethought': 'https://forethought.ai',
    'Inxide': 'https://inxide.ai',
    'GrowthBar': 'https://www.growthbarseo.com',
    'mesha': 'https://mesha.ai',
    'Hal9': 'https://hal9.com',
    'WRITER': 'https://writer.com',
    'Adobe Target': 'https://business.adobe.com/products/target/adobe-target.html',
    'Article Forge': 'https://www.articleforge.com',
    'Copysmith': 'https://copysmith.ai',
    'Sloyd': 'https://www.sloyd.ai',
    'Skai': 'https://www.skai.io',
    'SingleStore': 'https://www.singlestore.com',
    'MailMaestro': 'https://mailmaestro.com',
    'LongShot AI': 'https://www.longshot.ai',
    'Sunoh': 'https://sunoh.ai',
    'Breeze': 'https://www.hubspot.com/products/breeze',
    'Beautiful.ai': 'https://www.beautiful.ai',
    'NightCafe': 'https://creator.nightcafe.studio',
    'Replit': 'https://replit.com',
    'FlexClip': 'https://www.flexclip.com',
    'CoPilot AI': 'https://www.copilot.ai',
    'B12': 'https://www.b12.io',
    'eloomi': 'https://eloomi.com',
    'Copy.ai': 'https://www.copy.ai',
    'LOVO': 'https://lovo.ai',
    'memoQ TMS': 'https://www.memoq.com',
    'Opus Clip': 'https://www.opus.pro',
    'D-ID': 'https://www.d-id.com',
    'CredoHire': 'https://credohire.com',
    'Blocks': 'https://www.blocks.gov.uk',
    'AdCreative.ai': 'https://www.adcreative.ai',
    'vcita': 'https://www.vcita.com',
    'DeepSeek - AI Assistant': 'https://chat.deepseek.com',
}

with open('index.html', 'r') as f:
    content = f.read()

# Replace Google search links with real URLs
for tool_name, real_url in url_mapping.items():
    # Escape special regex characters in tool name
    escaped_name = tool_name.replace('.', r'\.').replace('&', r'&')
    search_name = escaped_name.replace(' ', '+')
    
    # Pattern for Google search link for this tool
    google_pattern = r'https://www\.google\.com/search\?q=' + re.escape(search_name) + r'\+AI\+tool'
    
    # Replace in href attributes
    content = re.sub(
        f'href="{google_pattern}"',
        f'href="{real_url}"',
        content
    )
    
    print(f"Updated: {tool_name} -> {real_url}")

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("\n✅ All placeholder links replaced with real URLs!")
