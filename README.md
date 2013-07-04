Copyright (c) 2013, Christopher Meng
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

FEEL FREE TO CREATE A ISSUE AND TELL ME WHICH PACKAGE YOU WANT TO BE INCLUDED IN Fedora!

# RPM specs for Fedora

## Branches

* EPEL - spec for EPEL
* master - spec for Fedora

## List

Let's see something real...

    monitorix                          # A free, open source, lightweight system monitoring tool(Needed by many SAs)
    mod_spdy                           # A SPDY module for the Apache HTTP server(Google Inc.)
    habari                             # A next-generation publishing platform
    reposurgeon                        # SCM Repository Manipulation Tool(Needed by me)
    w3perl                             # Web analytic tool for Web / FTP / Squid / CUPS and Mail servers
    youtube-dl                         # Small command-line program to download online videos(Painful)
    hadoop                             # A framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models
    ora2pg                             # Oracle to PostgreSQL database schema converter
    RemoteBox                          # Open Source VirtualBox Client with Remote Management
    nsnake                             # Classic snake game on console(Needed by fun)
    nblocks
    minised                            # A smaller, cheaper, faster SED implementation
    deepin-ui                          # Linux Deepin Graphics Library
    deepin-utils                       # Basic modules needed by most Linux Deepin applications
    lnav                               # Logfile Navigator
    tea                                # A text editor with the hundreds of features
    storeBackup                        # A very space efficient disk-to-disk backup suite 
    w3perl                             # Web analytic tool for Web / FTP / Squid / CUPS / DHCP and Mail servers
    sanewall                           # A powerful firewall builder
    cego                               # A relational and transactional database
    dhcpy6d                            # DHCPv6 server daemon
    gamgi                              # Build, View and Analyse Atomic Structures
    irker                              # IRC Message Relay
    lfcbase                            # Lemke Foundation Classes(Needed by cego)
    lfcxml                             # Lemke Foundation Classes XML Extensions(Needed by cego)
    lookat                             # A user-friendly text file viewer
    codecrypt                          # The post-quantum cryptography tool
    phrel                              # Per Host RatE Limiter
    nimrod                             # A statically typed, imperative programming language
    prwd                               # A tool can print reduced working directory
    darkhttpd                          # A secure, lightweight, fast, single-threaded HTTP/1.1 server
    edelib                             # Small and portable C++ library for EDE(Needed by EDE)
    ede                                # EDE(Equinox Desktop Environment)
    svni                               # Subversion interactive check-in wrapper
	tcpcopy                            # An online request replication tool(Needed by many companies)
	libserf                            # High-Performance Asynchronous HTTP Client Library(Needed by Subversion surf feature)
	ssh-installkeys                    #
	uthash                             # A hash table for C structures
	gcin                               # An input method focused on Chinese users
	
Perl stuffs:

    perl(DBD::Oracle)                  # Oracle database driver for the DBI module
	perl(File::Find::Object)           # Object oriented File::Find replacement 
	perl(Log::Handler)                 # Log messages to several outputs
	perl(Tapper)                       # A flexible and open test infrastructure(AMD Inc.)
	
	
	
Python stuffs:
	python-tvarage                     # Python client for the tvrage.com XML API
	
	
	
    ...                                # ...To be continued...

For more information, please refer to https://admin.fedoraproject.org/pkgdb/users/packages/cicku and relevant cgit repos hosted at http://pkgs.fedoraproject.org.

This list only contains the packages which has been reviewed and the last change are made when fedora-review becomes "+". So when I've imported them into the Fedora GIT infrastructure, I won't update the spec here. If you want to use my spec, please go to http://pkgs.fedoraproject.org and search the package name then you can see my spec in the tree.

See COPYING file for spec files license. Note that specs on http://pkgs.fedoraproject.org have the same license, although there are nothing in the specs of http://pkgs.fedoraproject.org say that they are licensed, you still need to keep in mind that they are written by myself, I don't include the license because I think it's ugly for the spec. Please notify any changes to the specs if you find some problems. Feel free to file a bug at http://bugzilla.redhat.com .
