# Imports
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up our App
st.set_page_config(page_title="Disk Data Sweeper", layout='wide')

st.title("Disk Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# File Uploader
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    uploaded_file = uploaded_files[0]  # Select first file
    file_ext = os.path.splitext(uploaded_file.name)[-1].lower()

    # Load the data
    if file_ext == ".csv":
        df = pd.read_csv(uploaded_file)
    elif file_ext == ".xlsx":
        df = pd.read_excel(uploaded_file)
    else:
        st.error(f"Unsupported file type: {file_ext}")
        st.stop()

    # Display file info
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    # Show 5 rows of our dataframe
    st.write("Preview the Head of the Dataframe")
    st.dataframe(df.head())

    # Data Cleaning Options
    st.subheader("Data Cleaning Options")

    if st.checkbox(f"Clean Data for {uploaded_file.name}"):
        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Remove Duplicates from {uploaded_file.name}"):
                df.drop_duplicates(inplace=True)
                st.write("Duplicates Removed!")

        with col2:
            if st.button(f"Fill Missing Values for {uploaded_file.name}"):
                numeric_cols = df.select_dtypes(include=['number']).columns
                df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                st.write("Missing Values have been Filled!")

                # Choose Specific Columns to Keep or Convert

                st.subheader("Select Columns to Convert")
                columns = st.multiselect(f"Choose Columns for {uploaded_files.name}", df.columns, default=df.columns)
                df =df[columns]



                #Create Some Visualization
                st.subheader("Price Data Visualization")
                if st.checkbox(f"Show Visualization for {uploaded_files.name}"):
                    st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

                    # Convert  the File -> CSV to Excel
                    # Select specific columns  
st.subheader("Select Columns to Convert")
columns = st.multiselect(f"Choose Columns for {uploaded_file.name}", df.columns, default=df.columns)  
df = df[columns]

                    # st.subheader("Conversion Options")
                    # conversion_type =st .radio(f"Convert {uploaded_files.name}to:",["CSV","Excel"], keys=uploaded_files.name)
                    # if st.button(f"Convert {uploaded_files.name}"):
                    #     from io import BytesIO
                        # Conversion Options
# st.subheader("Data Visualization")

if st.checkbox(f"Show Visualization for {uploaded_file.name}"):  # ✅ Corrected uploaded_files.name
    st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])

st.subheader("Conversion Options")
conversion_type = st.radio(f"Convert {uploaded_file.name} to:", ["CSV", "Excel"], key=uploaded_file.name)

if st.button(f"Convert {uploaded_file.name}"):
    buffer = BytesIO()

    # Check conversion type
    if conversion_type == "CSV":
        df.to_csv(buffer, index=False)
        file_name = uploaded_file.name.replace(file_ext, ".csv")
        mime_type = "text/csv"

    elif conversion_type == "Excel":
        df.to_excel(buffer, index=False)
        file_name = uploaded_file.name.replace(file_ext, ".xlsx")
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    # Reset buffer position
    buffer.seek(0)
    st.download_button(
        label=f"Download {file_name}",
        data=buffer,
        filename=file_name,  
        mime=mime_type
    )

    st.success("✅ File processed successfully!")


# buffer = BytesIO()

# # Check conversion type
# if conversion_type == "CSV":
#     df.to_csv(buffer, index=False)
#     file_name = uploaded_file.name.replace(file_ext, ".csv")
#     mime_type = "text/csv"

# elif conversion_type == "Excel":
#     df.to_excel(buffer, index=False)
#     file_name = uploaded_file.name.replace(file_ext, ".xlsx")
#     mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

# # Reset buffer position
# buffer.seek(0)
# st.download_button(
#     label=f"Download {uploaded_file.name} as {conversion_type}",
#     data=buffer,
#     filename=file_name,  # ✅ Corrected filename
#     mime=mime_type
# )

# st.success("✅ All files processed successfully!")

                        # buffer = BytesIO()
                        # if conversion_types == "CSV":
                        # df.to_csv(buffer,index=False)
                        # file_name =uploaded_files.name.replace(file_ext, ".csv")
                        # mime_type = "text/csv"

                        # elif conversion_type =="Excel":
                        #    df.to_excel(buffer,index=False)
                        # file_name = file.name.replace(file_ext,".xlsx")
                        # mime_type = application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        # buffer.seek(0)                      

                        #Download Button

#                           st.download_button(
#                             label=f"Download {uploaded_files.name} as {conversion_type}",
#                             data=buffer,
#                             filename=uploaded_files.name,
#                             mime=mime_type
#                         )
#                         st.success(" uppp All files process!")
# # import streamlit as st   # type: ignore
# import pandas as pd   # type: ignore
# import os
# from io import BytesIO

# # Set up our App
# st.set_page_config(page_title="Disk Data Sweeper", layout='wide')

# st.title("Disk Data Sweeper")
# st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization!")

# uploaded_files = st.file_uploader("upload you files (CVS or Excel):", type=["csv","xlsx"], accept_multiple_files=True)

# if uploaded_files:
#     # for file in uploaded_files:
#       uploaded_file = uploaded_files[0]  # Select first file
#             file_ext = os.path.splitext(uploaded_files.name)[-1] .lower() 

# Display info about the file
# st.write(f"**File Name:** {file.name}")  # ✅ Fixed function name
# st.write(f"**File Size:** {file.size / 1024:.2f} KB")  # ✅ Fixed function name & format

  
# # Display info about the file
# st.write(f"**File Name:** {file.name}")  # ✅ Fixed function name
# st.write(f"**File Size:** {file.size / 1024:.2f} KB")  # ✅ Fixed function name & format

        # elif file_ext == ".Xlsx":
        #     df = pd.read_excel(file)
        # else:
        #     st.error(f"Unsupported file type: {file_ext}")
        #     continue
         
        #  # Display info about the file

        # st.Write(f"**File Name:** {file.name}")
        # st.Write(f"**File Size:** {file.size/1024}")

        #Show 5 rows of our df
        # st.Write("Preview the Head of the Dataframe")
        # st.dataframe(df.head())

        # # Options for data cleaning
        # st.subheader("Data Cleaning Options")
        # if st.checkbox(f"Clean Data for{file.name}"):
        #     col1, col2 =st.columns(2)

        #     with col1:
        #           if st.button(f"Remove Duplicates form {file.name}"):
        #             df.drp_duplicates(inplace=True)
        #             st.Write("Duplicates Removed!")

        #             with col2:
        #                 if st.button(f"Fill Missing Values for {file.name}"):
        #                     numeric_cols = df.select_dtypes(include=['number']).columns
        #                     df[numeric_cols] =df[numeric_cols].fillna(df[numeric_cols].mean())
        #                     st.Write("Missing Values have been Filled!")



# Import streamlit as st
# import pandas as pd
# import os
# from io import BytesIO

   # else:
            #     st.error(f"Unsupported file type : {file_ext}")
# # St up our App
#  st.set_page_config(page_title="Disk Data sweeper",  layout='wide')
# st.title()
# st.write("Transfrom your files between CSV and Excel formats with built-in data cleaning and visualization!")