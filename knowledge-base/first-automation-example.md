# 🤖 Your First AI Automation Example

Welcome to your first AI automation project! This guide will walk you through creating a simple but powerful automation that demonstrates core AI concepts.

## 🎯 Overview

This example demonstrates:
- **Natural Language Processing (NLP)**: Understanding and processing text
- **API Integration**: Connecting to AI services
- **Automation Workflow**: Building end-to-end automation
- **Best Practices**: Writing maintainable automation code

## 🛠️ What We'll Build

An **Intelligent Email Categorizer** that:
1. Reads incoming emails
2. Uses AI to analyze content and sentiment
3. Automatically categorizes and prioritizes messages
4. Generates smart responses for common queries

## 📚 Prerequisites

- Basic Python knowledge
- An OpenAI API key (or alternative AI service)
- Python 3.8+ installed
- pip package manager

## 🚀 Step-by-Step Implementation

### Step 1: Set Up Your Environment

```bash
# Create a virtual environment
python -m venv ai-automation-env

# Activate it
# On Windows:
ai-automation-env\\Scripts\\activate
# On macOS/Linux:
source ai-automation-env/bin/activate

# Install required packages
pip install openai python-dotenv
```

### Step 2: Configure Your API Keys

Create a `.env` file in your project directory:

```env
OPENAI_API_KEY=your_api_key_here
EMAIL_ADDRESS=your_email@example.com
```

### Step 3: Write the Core Automation

Create `email_categorizer.py`:

```python
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def categorize_email(email_content):
    """
    Categorize an email using AI
    """
    prompt = f"""
    Analyze the following email and provide:
    1. Category (Urgent/Important/Normal/Spam)
    2. Sentiment (Positive/Neutral/Negative)
    3. Suggested action
    
    Email content:
    {email_content}
    
    Respond in JSON format.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an email analysis assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_response(email_content, category):
    """
    Generate a smart response based on email category
    """
    if category == "Spam":
        return "[Auto-archived]"
    
    prompt = f"""
    Generate a professional response to this email:
    {email_content}
    
    Keep it concise and helpful.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful email assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

# Example usage
if __name__ == "__main__":
    sample_email = """
    Hi there,
    
    I'm interested in learning more about your AI automation tools.
    Could you provide some documentation or a demo?
    
    Best regards,
    John Doe
    """
    
    # Categorize the email
    analysis = categorize_email(sample_email)
    print("Email Analysis:")
    print(analysis)
    print("\\n" + "="*50 + "\\n")
    
    # Generate a response
    response = generate_response(sample_email, "Important")
    print("Suggested Response:")
    print(response)
```

### Step 4: Run Your Automation

```bash
python email_categorizer.py
```

## 💡 Expected Output

You should see something like:

```
Email Analysis:
{
  "category": "Important",
  "sentiment": "Positive",
  "suggested_action": "Respond with information and schedule demo"
}

==================================================

Suggested Response:
Hi John,

Thank you for your interest in our AI automation tools! I'd be happy to help.

I can provide you with:
- Comprehensive documentation
- Video tutorials
- A personalized demo session

Would you prefer to schedule a quick call this week, or would you like me to send
over the materials first?

Best regards
```

## 🎓 Key Concepts Learned

1. **API Integration**: Connected to OpenAI's powerful language models
2. **Prompt Engineering**: Crafted effective prompts for specific tasks
3. **JSON Parsing**: Structured AI responses for easy processing
4. **Error Handling**: (Next step: add try-except blocks)
5. **Environment Variables**: Secured sensitive API keys

## 🚀 Next Steps

### Enhance Your Automation:

1. **Add Email Integration**:
   - Connect to Gmail API or IMAP
   - Process real emails automatically

2. **Improve Categorization**:
   - Train on your specific email patterns
   - Add custom categories

3. **Build a Dashboard**:
   - Visualize email trends
   - Track automation performance

4. **Add Scheduling**:
   - Run automation every 5 minutes
   - Use cron jobs or task schedulers

5. **Implement Learning**:
   - Store successful categorizations
   - Improve accuracy over time

## 📝 Best Practices

- ✅ **Always secure API keys** using environment variables
- ✅ **Handle errors gracefully** with try-except blocks
- ✅ **Log automation activities** for debugging
- ✅ **Test with sample data** before production use
- ✅ **Monitor API usage** to manage costs
- ✅ **Document your code** for future maintenance

## 🤝 Contributing

Improve this example:
- Add error handling
- Implement email integration
- Create unit tests
- Add more categorization logic
- Share your improvements!

## 📚 Additional Resources

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Python Email Libraries](https://docs.python.org/3/library/email.html)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [AI Automation Best Practices](../tools/sample-tool.py)

## ❓ Questions?

Join our [Discussions](../../discussions) and ask anything about this example!

---

**Congratulations!** 🎉 You've completed your first AI automation example. Now explore more in our [tools directory](../tools) and start building your own automations!

Happy coding! 🚀
