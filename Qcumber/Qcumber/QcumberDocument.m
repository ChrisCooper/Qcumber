//
//  QcumberDocument.m
//  Qcumber
//
//  Created by Chris Cooper on 11-11-21.
//  Copyright (c) 2011 Chris Cooper. All rights reserved.
//

#import "QcumberDocument.h"

@implementation QcumberDocument

- (id)init
{
    self = [super init];
    if (self) {
        // Add your subclass-specific initialization here.
        // If an error occurs here, return nil.
    }
    return self;
}

- (NSString *)windowNibName
{
    // Override returning the nib file name of the document
    // If you need to use a subclass of NSWindowController or if your document supports multiple NSWindowControllers, you should remove this method and override -makeWindowControllers instead.
    return @"QcumberDocument";
}

- (void)windowControllerDidLoadNib:(NSWindowController *)aController
{
    [super windowControllerDidLoadNib:aController];
    // Add any code here that needs to be executed once the windowController has loaded the document's window.
}

- (NSData *)dataOfType:(NSString *)typeName error:(NSError **)outError
{
    /*
     Insert code here to write your document to data of the specified type. If outError != NULL, ensure that you create and set an appropriate error when returning nil.
    You can also choose to override -fileWrapperOfType:error:, -writeToURL:ofType:error:, or -writeToURL:ofType:forSaveOperation:originalContentsURL:error: instead.
    */
    NSException *exception = [NSException exceptionWithName:@"UnimplementedMethod" reason:[NSString stringWithFormat:@"%@ is unimplemented", NSStringFromSelector(_cmd)] userInfo:nil];
    @throw exception;
    return nil;
}

- (BOOL)readFromData:(NSData *)data ofType:(NSString *)typeName error:(NSError **)outError
{
    /*
    Insert code here to read your document from the given data of the specified type. If outError != NULL, ensure that you create and set an appropriate error when returning NO.
    You can also choose to override -readFromFileWrapper:ofType:error: or -readFromURL:ofType:error: instead.
    If you override either of these, you should also override -isEntireFileLoaded to return NO if the contents are lazily loaded.
    */
    NSException *exception = [NSException exceptionWithName:@"UnimplementedMethod" reason:[NSString stringWithFormat:@"%@ is unimplemented", NSStringFromSelector(_cmd)] userInfo:nil];
    @throw exception;
    return YES;
}

+ (BOOL)autosavesInPlace
{
    return YES;
}

@end





















#import "SplitViewAppDelegate.h"
#import <Appkit/NSLayoutConstraint.h>

@implementation SplitViewAppDelegate

@synthesize window;

- (void)awakeFromNib {
    
    [yellowLabel setTranslatesAutoresizingMaskIntoConstraints:NO];
    [labelAlignedToTopOfYellowView setTranslatesAutoresizingMaskIntoConstraints:NO];
    NSView *yellowView = [yellowLabel superview];
    NSView *contentView = [[self window] contentView];
    
    // Center the yellow label
    [splitView addConstraint:[NSLayoutConstraint constraintWithItem:yellowLabel attribute:NSLayoutAttributeCenterX relatedBy:NSLayoutRelationEqual toItem:splitView attribute:NSLayoutAttributeCenterX multiplier:1.0 constant:0]];
    [splitView addConstraint:[NSLayoutConstraint constraintWithItem:yellowLabel attribute:NSLayoutAttributeCenterY relatedBy:NSLayoutRelationEqual toItem:yellowView attribute:NSLayoutAttributeCenterY multiplier:1.0 constant:0]];
    
    // don't let the splitview get too small for the label
    [splitView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"|-(>=0)-[yellowLabel]-(>=0)-|" options:0 metrics:nil views:NSDictionaryOfVariableBindings(yellowLabel)]];
    
    // Make the labelAlignedToTopOfYellowView stick to the outside right edge of the splitview, aligned with the top of the yellow view
    [contentView addConstraint:[NSLayoutConstraint constraintWithItem:yellowView attribute:NSLayoutAttributeTop relatedBy:NSLayoutRelationEqual toItem:labelAlignedToTopOfYellowView attribute:NSLayoutAttributeTop multiplier:1.0 constant:0]];
    [contentView addConstraints:[NSLayoutConstraint constraintsWithVisualFormat:@"[splitView][labelAlignedToTopOfYellowView]" options:0 metrics:nil views:NSDictionaryOfVariableBindings(splitView, labelAlignedToTopOfYellowView)]];
    
    [super awakeFromNib];
}

@end