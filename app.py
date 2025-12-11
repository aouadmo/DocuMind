"""
DocuMind: Universal AI Document Extraction & Analysis Dashboard
Main Streamlit application.
"""
import streamlit as st
import pandas as pd
import json
from config import Config
from extractor import DocumentExtractor
from document_processor import DocumentProcessor
from utils import validate_file, format_json_for_display


# Page configuration
st.set_page_config(
    page_title="DocuMind",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if 'extracted_data' not in st.session_state:
        st.session_state.extracted_data = None
    if 'text_content' not in st.session_state:
        st.session_state.text_content = None
    if 'file_name' not in st.session_state:
        st.session_state.file_name = None


def main():
    """Main application function."""
    initialize_session_state()
    
    # Header
    st.markdown('<div class="main-header">📄 DocuMind</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Universal AI Document Extraction & Analysis Dashboard</div>',
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Extraction mode selection
        extraction_mode = st.selectbox(
            "Select Extraction Mode",
            options=list(Config.EXTRACTION_MODES.keys()),
            help="Choose the type of document you want to analyze"
        )
        
        st.divider()
        
        # Information
        st.subheader("ℹ️ About")
        mode_descriptions = {
            "Resume Parsing": "Extract candidate information, skills, and experience from resumes",
            "Invoice Data": "Extract invoice details, amounts, and vendor information",
            "Sentiment Analysis": "Analyze text sentiment, tone, and key themes"
        }
        st.info(mode_descriptions[extraction_mode])
        
        st.divider()
        
        # File requirements
        st.subheader("📋 Requirements")
        st.write(f"**Max file size:** {Config.MAX_FILE_SIZE_MB}MB")
        st.write(f"**Allowed formats:** {', '.join(Config.ALLOWED_EXTENSIONS)}")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload Document")
        
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['pdf', 'txt'],
            help="Upload a PDF or TXT file for analysis"
        )
        
        if uploaded_file:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            # Validate file
            is_valid, error_msg = validate_file(uploaded_file)
            
            if not is_valid:
                st.error(f"❌ {error_msg}")
                return
            
            # Show file info
            file_size_kb = uploaded_file.size / 1024
            st.caption(f"Size: {file_size_kb:.2f} KB")
    
    with col2:
        st.subheader("🚀 Actions")
        
        analyze_button = st.button(
            "🔍 Analyze Document",
            type="primary",
            disabled=uploaded_file is None,
            use_container_width=True
        )
    
    # Process document when button is clicked
    if analyze_button and uploaded_file:
        try:
            with st.spinner('🔄 Processing document...'):
                # Extract text from document
                processor = DocumentProcessor()
                text_content = processor.process_file(uploaded_file)
                st.session_state.text_content = text_content
                st.session_state.file_name = uploaded_file.name
            
            with st.spinner('🤖 AI is analyzing...'):
                # Extract data using AI
                extractor = DocumentExtractor()
                extraction_type = Config.EXTRACTION_MODES[extraction_mode]
                extracted_data = extractor.extract_data(text_content, extraction_type)
                st.session_state.extracted_data = extracted_data
            
            st.success("✅ Analysis complete!")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            return
    
    # Display results if available
    if st.session_state.extracted_data:
        st.divider()
        st.header("📊 Extraction Results")
        
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["📋 Table View", "🔤 JSON View", "📥 Download"])
        
        with tab1:
            # Display as DataFrame
            df = pd.json_normalize(st.session_state.extracted_data)
            st.dataframe(df, use_container_width=True)
        
        with tab2:
            # Display as formatted JSON
            formatted_data = format_json_for_display(st.session_state.extracted_data)
            st.json(formatted_data)
        
        with tab3:
            st.subheader("Download Options")
            
            col_a, col_b = st.columns(2)
            
            with col_a:
                # Download as JSON
                json_str = json.dumps(st.session_state.extracted_data, indent=2)
                st.download_button(
                    label="📄 Download JSON",
                    data=json_str,
                    file_name=f"{st.session_state.file_name}_extracted.json",
                    mime="application/json",
                    use_container_width=True
                )
            
            with col_b:
                # Download as CSV
                df = pd.json_normalize(st.session_state.extracted_data)
                csv = df.to_csv(index=False)
                st.download_button(
                    label="📊 Download CSV",
                    data=csv,
                    file_name=f"{st.session_state.file_name}_extracted.csv",
                    mime="text/csv",
                    use_container_width=True
                )


if __name__ == "__main__":
    try:
        Config.validate()
        main()
    except ValueError as e:
        st.error(f"⚠️ Configuration Error: {str(e)}")
        st.info("Please create a .env file with your OPENAI_API_KEY. See .env.example for reference.")

