"""
Design a photo album application where user can store pictures and share among the others using their email ids. You need to provide high level design for server and client

"""

'''
Client needs:
    - upload photos
    - arrange photos into albums / manage photos
    - add metadata to photos
    - download photos
    - login accounts (using email id)

Server needs:
    - database of photos/links to photos with metadata
        - fleet of read-only slaves
    - storage to store photos
        - distributed storage with redundancy
    - web frontends
        - loadbalanced with queue and scalable groups
        - hosted in different regions with traffic directed by route tables
    - cache 1: recently accessed photos
    - cache 2: frequently accessed photos
    - redundancy and security

'''
