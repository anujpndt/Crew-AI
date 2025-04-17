from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

## Research Task
research_task = Task(
    description=(
        "Find the latest Barack Obama speech on the channel. "
        "Search for the video with title 'Barack Obama Inspirational Speech with Subtitles || "
        "One of the best English speeches ever 2023'. "
        "Extract the transcript and key points from this video."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the video content.',
    tools=[yt_tool],
    agent=blog_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Using the research provided by the Blog Researcher, create a well-structured blog post "
        "about Barack Obama's inspirational speech. Focus on the key messages, "
        "inspirational quotes, and the context of the speech. "
        "Make it engaging and educational for readers."
    ),
    expected_output='A complete blog post summarizing the speech with proper formatting, headings, and quotes.',
    tools=[yt_tool],
    agent=blog_writer,
    async_execution=False,
    dependencies=[research_task],  # Added dependency on research task
    output_file='obama-speech-blog-post.md'  # More specific filename
)